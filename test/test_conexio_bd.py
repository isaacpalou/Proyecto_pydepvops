
from main import main
import pytest


@pytest.mark.datos
def test_main():
    assert isinstance(main(), list)
