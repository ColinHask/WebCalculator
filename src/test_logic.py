import pytest
import logic
from logic import calculate_mean
from logic import calculate_standard_deviation
from logic import calculate_z_score


def test_CalculateMean_NormalList_CorrectNumber():
    result = calculate_mean([1, 2, 3])
    assert result == 2

def test_CalculateMean_EmptyList_ValueError():
    with pytest.raises(ValueError):
        calculate_mean([])

def test_CalculateStandardDeviation_NormalList_CorrectNumber():
    result = calculate_standard_deviation([1, 2, 3, 4, 5])
    assert result == 1.4142135623730951

def test_CalculateStandardDeviation_EmptyList_ValueError():
    with pytest.raises(ValueError):
        calculate_standard_deviation([])

def test_CalculateZscore_NormalValues_CorrectNumber():
    result = calculate_z_score(5,3,2)
    assert result == 1

def test_CalculateZscore_DivideBy0_ValueError():
    with pytest.raises(ValueError):
        calculate_z_score(2,6,0)



