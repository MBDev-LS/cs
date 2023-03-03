import os
from pathlib import Path
import pkg_resources
from newsai.utils.nlogger import Log

_ROOT_PATH = os.path.abspath(Path(__file__))
_DATA_PATH = os.path.join(Path(_ROOT_PATH).parents[2], 'data')
