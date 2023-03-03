import logging
from logging import (DEBUG, INFO, WARNING, ERROR, CRITICAL)


class Log(logging.Logger):
    lvl = DEBUG

    def __new__(cls, module_name='newsai'):
        self = logging.getLogger(module_name)
        self.setLevel(cls.lvl)
        if module_name != "asyncio":
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        else:
            formatter = logging.Formatter(
                '%(asctime)s - newsai.async_download - %(levelname)s - %(message)s')

        ch = logging.StreamHandler()
        ch.setLevel(cls.lvl)
        ch.setFormatter(formatter)

        fh = logging.FileHandler('log.txt', mode='a')
        fh.setLevel(cls.lvl)
        fh.setFormatter(formatter)

        self.addHandler(ch)
        self.addHandler(fh)
        return self

    @classmethod
    def set_lvl(cls, lvl=DEBUG) -> None:
        cls.lvl = lvl
