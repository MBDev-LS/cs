"""
underlying storage classes used by async_download to format
news stories from HTTP response
"""


from collections import defaultdict
from datetime import datetime
from typing import Union, Optional, List, Iterable
import pathlib
import re
import pandas as pd

__all__ = ["Url", "Path", "NewsDumpDict",
           "StoryHolderDict", "StoryDict", "Singleton", "NewsDump"]

Url = str
Path = Union[str, pathlib.Path]


class NewsDumpDict(dict):
    """
    preformatted dict
    """

    def __repr__(self):
        return "{" + "\n".join("{!r}: {!r},".format(k, v)
                               for k, v in self.items()) + "}"


class StoryHolderDict(dict):
    """
    pre-formatted dictionary with to_pandas functionality
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        rep_str = ""
        for key, value in self.items():
            if key == "stories":
                rep_str = rep_str + "".join("{!r}:\n{!r}".format(key, value))
            else:
                rep_str = rep_str + "".join("{!r}: {!r},".format(key, value))
        return rep_str

    def to_pandas(self, cols: Iterable[str] = None) -> pd.DataFrame:
        dataframe = pd.DataFrame(self['stories'])
        if cols is None:
            cols = ('datetime', 'url', 'alias')
        for key, val in self.items():
            if key in cols:
                dataframe[key] = val
        return dataframe


class StoryDict(defaultdict):
    """
    returns default dictionary with H0, H1, H2
    or keys from kwargs
    StoryDict('a', 'b', 'c') -> {'H0': 'a', 'H1': 'b', 'H2': 'c'}
    """

    def __init__(self, *args, **kwargs):
        super().__init__(lambda: None, **kwargs)

        new_elements = [arg for arg in args if arg is not None]

        for i, _ in enumerate(new_elements):
            self.__setitem__('H' + str(i), new_elements[i])

    def __repr__(self):
        return str(dict(self))


def ndict(*args, **kwargs) -> Optional[List[StoryDict]]:
    """
    IN: ndict('Story a', 'Story a details\n\n\nStory b')
    OUT: {'H0': ['Story a', 'Story a details'], 'H1': ['Story b']}
    """
    if kwargs:
        out = [StoryDict(**kwargs)]
    else:
        in_story_vals = list(StoryDict(*args, **kwargs).values())
        split_args = []
        max_len = 1
        for i in in_story_vals:
            spl = re.split('\n+', i)
            num_lines = len(spl)
            split_args.append(spl)
            if num_lines > max_len:
                max_len = num_lines
        expanded_list = []
        for i in range(max_len):
            values_at_level = []
            for j in split_args:
                try:
                    values_at_level.append(j[i])
                except IndexError:
                    pass
            expanded_list.append(values_at_level)
        out = []
        for i in expanded_list:
            if any(i):
                out.append(StoryDict(*i))
    if any(out):
        return out


class Singleton(type):
    """
    Singleton metaclass for NewsDump
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]


class NewsDump(metaclass=Singleton):
    """
    replace current strucure:
    list of default dicts
    dict_keys(['id', 'datetime', 'url', 'alias', 'name',
              'cls_name', 'features', 'stories'])
    stories is a list of dictionaries each like the following
    {'H0': 'LiveLiveUS passes two million cases as states report rise',
        'H1': 'Daily infections are still...', 'H2': None}
    """

    story_dump = NewsDumpDict()

    def __init__(self,
                 config_id: int,
                 url: Url,
                 alias: Optional[str] = None,
                 name: Optional[str] = None,
                 cls_name: Optional[str] = None,
                 features: Optional[str] = None):
        self.story_dump[config_id] = StoryHolderDict(
            datetime=datetime.now(),
            url=url,
            alias=alias,
            name=name,
            cls_name=cls_name,
            features=features,
            stories=[])

    def __repr__(self):
        return f'{self.__class__.__name__}'

    @staticmethod
    def __len__():
        return len(NewsDump.story_dump)

    @staticmethod
    def add_story(config_id, *args, **kwargs):
        """
        adds story to NewsDump.story_dump
        """
        to_append = ndict(*args, **kwargs)
        if to_append:
            for i in to_append:
                NewsDump.story_dump[config_id]['stories'].append(i)
