"""
News crawler classes
"""

__all__ = ["News", "HistoricalNews"]

import sys
from os.path import dirname, join, realpath, basename
from typing import List, Dict
from json import load, loads
import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from bs4.element import Tag
from .utils.ipython import run_from_ipython
from .utils.nlogger import Log
from .newstypes import NewsDump, Url, Path, StoryHolderDict, StoryDict

LOGGER = Log("asyncio")

assert sys.version_info >= (3, 7), "Requirement: Python 3.7+."


class News():
    """
    News crawler class
    usage: see newsai\\examples
    """

    def __init__(self,
                 j_name: Path = 'url_config.json',
                 **kwargs: str):

        self.j_name = j_name
        self.find_futures_list: List[asyncio.Future] = []
        self.responses: Dict = {}
        self.j_dict = self.filter_by_val(
            self.load_json(j_name), **kwargs
        )

    def __call__(self) -> List:
        try:
            assert not run_from_ipython
            return self.run_async()
        except AssertionError:
            raise AttributeError(
                "If called iPython run_async() function should be called " +
                "directly. e.g. await News().run_async()")

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'config: {basename(self.j_name)})')

    @staticmethod
    def filter_by_val(j_dict: Dict, **kwargs: str) -> Dict:
        """
        we can pass in a list of arguments allowing
        us to filter the json by any values we like
        """
        def _filter_dict(j_dict, f_by, f_elem):
            return {key: val for key, val in j_dict.items()
                    if val[f_by] == f_elem}

        for key, val in kwargs.items():
            j_dict = _filter_dict(j_dict, key, val)

        return j_dict

    @staticmethod
    def load_json(j_name: Dict) -> Dict:
        """
        reads url_config json
        """
        # if not run_from_ipython:
        json_path = join(
            dirname(realpath(__file__)), j_name
        )
        with open(json_path) as config_file:
            return load(config_file)

    def add_futures(self, j_file: Path):
        """
        builds the futures list for the retrieval and search of stories
        """
        for key, val in j_file.items():
            self.build_futures_get(val['url'])
            self.build_futures_search(int(key), val)

    def build_futures_get(self, url: Url):
        """
        builds responses dict with futures
        when run the futures return the response texts of the GET requests
        """
        if url not in self.responses:
            self.responses[url] = asyncio.ensure_future(
                self.exec_get(
                    url=url)
            )

    def build_futures_search(self, config_id: int, url_info: Dict):
        """
        builds find_futures_list for search of GET requests reponse texts
        """
        try:
            self.find_futures_list.append(
                asyncio.ensure_future(self.exec_find(
                    url_info["url"],
                    url_info["alias"],
                    url_info["name"],
                    url_info["cls_name"],
                    url_info["features"],
                    config_id
                )))
        except KeyError:
            self.find_futures_list.append(
                asyncio.ensure_future(self.json_selector(
                    url_info["url"],
                    url_info["alias"],
                    url_info["json_key"],
                    config_id
                )))

    def run_async(self) -> StoryHolderDict:
        """
        creates and runs futures lists for GET requests and search
        """
        self.add_futures(self.j_dict)
        loop = asyncio.get_event_loop()
        get_url_futures = asyncio.gather(
            *[f for f in self.responses.values()])
        find_text_futures = asyncio.gather(
            *[f for f in self.find_futures_list])

        final_future = asyncio.gather(get_url_futures, find_text_futures)

        if not run_from_ipython:
            loop.run_until_complete(final_future)
        else:
            asyncio.ensure_future(final_future)
        return NewsDump.story_dump

    async def exec_get(self, url: Url):
        """
        awaits GET requests
        """
        LOGGER.debug(f'getting {url}')
        async with ClientSession() as session:
            self.responses[url] = await self.fetch_stories(
                session, url
            )

    async def exec_find(self, url: Url, alias: str,
                        name: str, cls_name: str,
                        features: str, config_id: int):
        """
        called by build_futures_search when no api provided
        """
        await self.responses[url]
        await self.find_stories(
            url,
            alias,
            self.responses[url],
            name,
            cls_name,
            features,
            config_id
        )

    async def json_selector(self, url: Url, alias: str,
                            json_key: Dict, config_id: int = 0):
        """
        called by build_futures_search when api provided
        """
        await self.responses[url]
        json_out = loads(self.responses[url])

        if isinstance(json_key['filter'], str):
            json_key['filter'] = [json_key['filter']]
        results = json_out
        for fltr in json_key['filter']:
            results = results[fltr]

        news_dump = NewsDump(config_id, url, alias)

        for story in results:
            story_dict = StoryDict()
            for k, val in json_key['attribute'].items():
                if k in ('H0', 'H1', 'H2'):
                    new_val = story[val].encode(
                        'ascii', errors='ignore').decode('utf-8')
                else:
                    new_val = story[val]
                story_dict.update(**{k: new_val})
            news_dump.add_story(config_id, **story_dict)

    @staticmethod
    async def fetch_stories(session: ClientSession, url: Url):
        """
        awaits HTTP requests
        """
        async with session.get(url) as response:
            LOGGER.info(f"Status: {response.status}")
            return await response.text()

    @staticmethod
    async def find_stories(url: Url, alias: str,
                           response_text: str, name: str,
                           cls_name: str, features: str,
                           config_id: int = 0
                           ):
        """
        searches for story html classes in request response text
        for websites w/o apis
        """
        news_dump = NewsDump(config_id, url, alias, name, cls_name, features)

        LOGGER.debug(f"searching url: {url}")
        soup = BeautifulSoup(response_text.encode(
            'ascii', errors='ignore').decode('utf-8'), features=features)

        def _return_sibling(tag: Tag):
            try:
                return tag.text
            except AttributeError:
                return None

        if isinstance(cls_name, str):
            cls_name = [cls_name]

        for cla in cls_name:
            element = soup.find_all(name, {"class": cla})
            if len(element) == 0:
                LOGGER.warning('No output returned for id: ' +
                               '{0}, cls_name: {1}, url: {2}'.format(
                                   config_id, cla, url))
            for i in element:
                news_dump.add_story(config_id,
                                    _return_sibling(i.previousSibling),
                                    _return_sibling(i),
                                    _return_sibling(i.nextSibling)
                                    )


class HistoricalNews(News):
    """
    inherits News crawler class using year and month as arguments
    """

    def __init__(self,
                 year: int,
                 month: int,
                 j_name: Path = 'url_hist_config.json',
                 **kwargs: str):
        super().__init__(j_name=j_name, **kwargs)
        self.year = year
        self.month = month
        for element in self.j_dict.values():
            element["url"] = element["url"].format(year, month)

    def __call__(self) -> List:
        return self.run_async()

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'config: {basename(self.j_name)}, '
                f'year: {self.year}, month: {self.month})')
