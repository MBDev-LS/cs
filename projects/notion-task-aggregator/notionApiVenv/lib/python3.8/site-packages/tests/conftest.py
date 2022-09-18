import pytest

from pytion import Notion, setup_logging
from tests.fixtures import *


token = "secret_b3p8YOa25T1h9AscYVox8c5XO7yH8gh0tn7q3cfnnd0"


@pytest.fixture(scope="session")
def no():
    setup_logging("warning")
    return Notion(token)
