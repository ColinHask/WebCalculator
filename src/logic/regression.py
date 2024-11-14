import math


def linear_regression(xy_list):
    """
    intakes a list of number pairs (e.g., [(x1,y1),...,(xn,yn)]) and returns the estimated slope and
    then uses the calculations of that slope to return the predicted y intercept
    """

    number_of_pairs = len(xy_list)
    try:
        # summing up all the x elements in each pair and storing it in a total_x value
        total_x = 0
        for i in xy_list:
            total_x += i[0]

        # summing up all the y elements in each pair and storing it in a total_y value
        total_y = 0
        for i in xy_list:
            total_y += i[1]

        # obtaining the average for both elements in pairs
        average_x = total_x / number_of_pairs
        average_y = total_y / number_of_pairs

        # the formula for estimating slope is a big fraction. For clarity the calculations for numerator are stored
        # in a numerator variable and the calculations for denominator are stored in a denominator variable.
        numerator_sum = 0
        denominator_sum = 0
        for i in xy_list:
            # each x and y element in each pair has its average subtracted from it
            x_difference = i[0] - average_x
            y_difference = i[1] - average_y
            # total numerator and denominator sum up to a result by the end of the loop
            numerator_sum += x_difference * y_difference
            denominator_sum += x_difference ** 2

        # slope is calculated from numerator and denominator calculations
        estimated_slope = numerator_sum / denominator_sum

        # using slope equation, the y intercept is calculated
        y_intercept = average_y - estimated_slope * average_x

        return estimated_slope, y_intercept

    except ZeroDivisionError:
        # checking for division by zero exception
        raise ValueError("you cannot divide by zero")


def predict_y(x, m, b):
    """
    intakes three variables which I purposely named x, m and b since this calculation using form y = mx + b standard
    linear polynomial equation. Finally, it returns the value of the function (i.e., y) using the slope, the x value
    and the y intercept.
    """
    try:
        predicted_y = (m * x) + b
        return predicted_y

    except TypeError:
        # checking for non-numerical inputs
        raise ValueError("all user inputs have to be numbers")