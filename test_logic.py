import pytest
import logic
from logic import calculate_mean


def test_CalculateMean_NormalList_CorrectNumber():
    result = calculate_mean([1, 2, 3])
    assert result == 2

def test_CalculateMean_EmptyList_Exception():
    with pytest.raises(ValueError):
        calculate_mean([])
