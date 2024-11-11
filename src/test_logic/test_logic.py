import pytest

# statistics.py imports
from src.logic.statistics import mean
from src.logic.statistics import standard_deviation
from src.logic.statistics import z_score

# regression.py imports
from src.logic.regression import linear_regression
from src.logic.regression import predict_y


#######################################################################################


@pytest.mark.parametrize("tested_mean, expected_mean", [([4, 5, 6], 5), ([7, 8, 9], 8), ([10, 11, 12], 11)])
def test_calculate_mean(tested_mean, expected_mean):
    """
    Testing mean with three lists and checking the output with expected output
    """
    # act
    actual_mean = mean(tested_mean)
    # assert
    assert actual_mean == expected_mean


# testing mean for empty list condition in case user inputs nothing
def test_calculate_mean_empty_list():
    with pytest.raises(ValueError):
        mean([])


@pytest.mark.parametrize("tested_standard_deviation, expected_standard_deviation",
                         [([1, 2, 3, 4, 5], 1.4142135624), ([7, 8, 9], 0.8164965809), ([10, 15, 20], 4.0824829046)])
def test_standard_deviation(tested_standard_deviation, expected_standard_deviation):
    """
    testing standard deviation with three different lists and comparing expected outputs with actual outputs
    """
    # act
    actual_standard_deviation = round(standard_deviation(tested_standard_deviation), 10)
    # assert
    assert round(actual_standard_deviation, 10) == round(expected_standard_deviation, 10)


# testing standard deviation for empty list conditon in case user enters nothing
def test_standard_deviation_empty_list():
    with pytest.raises(ValueError):
        standard_deviation([])


@pytest.mark.parametrize("tested_value, tested_average, tested_variation, expected_z_score",
                         [(12, 8, 2, 2),
                          (7, 5, 1.5, 1.3333333333),
                          (15, 10, 3, 1.6666666666)])
def test_z_score(tested_value, tested_average, tested_variation, expected_z_score):
    """
    testing z score with three separate triples of numbers and comparing expected out put with actual output
    """
    # act
    actual_z_score = z_score(tested_value, tested_average, tested_variation)
    # assert
    assert actual_z_score == expected_z_score


# testing z score for division by zero exception where variance (standard deviation) is zero
def test_z_score_empty_list():
    with pytest.raises(ValueError):
        z_score(2, 6, 0)


#######################################################################################

@pytest.mark.parametrize("tested_list, expected_slope, expected_y_intercept",
                         [([(1.47, 52.21), (1.5, 53.12), (1.52, 54.48), (1.55, 55.84), (1.57, 57.2), (1.6, 58.57),
                            (1.63, 59.93), (1.65, 61.29), (1.68, 63.11), (1.7, 64.47), (1.73, 66.28), (1.75, 68.1),
                            (1.78, 69.92), (1.8, 72.19), (1.83, 74.46)], 61.2721865421, -39.0619559188),
                          ([(1, 2), (2, 3), (3, 4), (4, 5)], 1, 1), ([(1, 5), (2, 3), (3, 1), (4, -1)], -2, 7)])
def test_linear_regression(tested_list, expected_slope, expected_y_intercept):
    """
    testing linear regression with three different lists of pairs. The first list is big and used from github example.
    All are then compared to expected output vs actual output. Regression calculates both the slope and the y intercept
    so both have an expected output thats compared the actual output.
    """
    # act
    actual_slope, actual_y_intercept = linear_regression(tested_list)
    # assert
    assert round(actual_slope, 10) == round(expected_slope, 10)
    assert round(actual_y_intercept, 10) == round(expected_y_intercept, 10)


# testing linear regression for a null input
def test_linear_regression_empty_list():
    with pytest.raises(ValueError):
        linear_regression([])


@pytest.mark.parametrize("tested_x, tested_m, tested_b, expected_predicted_y",
                         [(1.535, 61.2721865421, -39.0619559188, 54.9908504232),
                          (3.14159, 2.71828, 0, 8.5397212652), (0, 12345, 2, 2)])
def test_predict_y(tested_x, tested_m, tested_b, expected_predicted_y):
    """
    testing predicted y with three separate testes each with an expected output
    """
    # act
    actual_predicted_y = predict_y(tested_x, tested_m, tested_b)
    # assert
    assert round(actual_predicted_y, 10) == round(expected_predicted_y, 10)


# testing predicted y value in case the user enters nothing for the x value.
def test_predict_y_empty_list():
    with pytest.raises(ValueError):
        predict_y(None, 61.272186542107434, -39.061955918838656)
