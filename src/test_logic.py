import pytest
import logic
from logic import calculate_mean
from logic import calculate_standard_deviation
from logic import calculate_z_score
from logic import compute_single_linear_regression
from logic import predict_y_from_linear_regression

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

####

def test_compute_single_linear_regression():
    test_list = [(1.47, 52.21), (1.5, 53.12), (1.52, 54.48), (1.55, 55.84), (1.57, 57.2), (1.6, 58.57), (1.63, 59.93),
                (1.65, 61.29), (1.68, 63.11), (1.7, 64.47), (1.73, 66.28), (1.75, 68.1), (1.78, 69.92), (1.8, 72.19),
                (1.83, 74.46)]
    m_slope, b_intercept = compute_single_linear_regression(test_list)
    assert m_slope == 61.272186542107434
    assert b_intercept == -39.061955918838656

def test_predict_y_from_linear_regression():

    x_given_value = 1.535
    m_slope = 61.272186542107434
    b_intercept = -39.061955918838656

    result = predict_y_from_linear_regression(x_given_value, m_slope, b_intercept)
    assert result == 54.990850423296244


