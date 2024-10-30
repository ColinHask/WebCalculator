import pytest

# logic.py imports
import statistics
from statistics import mean
from statistics import standard_deviation
from statistics import z_score

# regression.py imports
import regression
from regression import linear_regression
from regression import predict_y


#######################################################################################


def test_calculate_mean():
    result = mean([1, 2, 3])
    assert result == 2


def test_calculate_mean_empty_list():
    with pytest.raises(ValueError):
        mean([])


def test_standard_deviation():
    result = standard_deviation([1, 2, 3, 4, 5])
    assert result == 1.4142135623730951


def test_standard_deviation_empty_list():
    with pytest.raises(ValueError):
        standard_deviation([])


def test_z_score():
    result = z_score(5, 3, 2)
    assert result == 1


def test_z_score_empty_list():
    with pytest.raises(ValueError):
        z_score(2, 6, 0)


#######################################################################################


def test_linear_regression():
    test_list = [(1.47, 52.21), (1.5, 53.12), (1.52, 54.48), (1.55, 55.84), (1.57, 57.2), (1.6, 58.57), (1.63, 59.93),
                 (1.65, 61.29), (1.68, 63.11), (1.7, 64.47), (1.73, 66.28), (1.75, 68.1), (1.78, 69.92), (1.8, 72.19),
                 (1.83, 74.46)]

    expected_slope, expected_y_intercept = linear_regression(test_list)

    assert round(expected_slope, 10) == round(61.272186542107434, 10)
    assert round(expected_y_intercept, 10) == round(-39.061955918838656, 10)


def test_linear_regression_empty_list():
    with pytest.raises(ValueError):
        linear_regression([])


def test_predict_y():
    x_given_value = 1.535
    m_slope = 61.272186542107434
    b_intercept = -39.061955918838656

    result = predict_y(x_given_value, m_slope, b_intercept)
    assert result == 54.990850423296244


def test_predict_y_empty_list():
    with pytest.raises(ValueError):
        predict_y(None, 61.272186542107434, -39.061955918838656)
