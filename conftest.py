import pytest
from helpers.onp_handler import ONPHandler
from config import prod
from main import Data


@pytest.fixture(name="onp_handler")
def onp_handler_fixture():
    onp_handler = ONPHandler(digits=prod.digits, operations=prod.operations)
    return onp_handler


@pytest.fixture(name="data_handler")
def data_fixture():
    data_handler = Data()
    return data_handler

