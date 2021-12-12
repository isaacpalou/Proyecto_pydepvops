
from main import main
import pytest

from src.Logica_python.filter import high_filter, low_filter, medium_filter

@pytest.mark.filtro_listas
def test_low_filter():
    assert isinstance(low_filter(), list)

@pytest.mark.filtro_listas
def test_medium_filter():
    assert isinstance(medium_filter(), list)

@pytest.mark.filtro_listas
def test_high_filter():
    assert isinstance(high_filter(), list)