# pip install pytest pytest-cov
import pytest
from main import Fruta


@pytest.fixture()
def minha_fruta():
    return Fruta("maçã")


@pytest.fixture()
def cesta_frutas(minha_fruta):
    return [Fruta("banana"), minha_fruta]
