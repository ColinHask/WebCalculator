import math


def linear_regression(xy_list):
    number_of_pairs = len(xy_list)
    try:
        total_x = 0
        for i in xy_list:
            total_x += i[0]
        total_y = 0
        for i in xy_list:
            total_y += i[1]

        average_x = total_x / number_of_pairs
        average_y = total_y / number_of_pairs

        numerator_sum = 0
        denominator_sum = 0
        for i in xy_list:
            x_difference = i[0] - average_x
            y_difference = i[1] - average_y

            numerator_sum += x_difference * y_difference
            denominator_sum += x_difference ** 2

        estimated_slope = numerator_sum / denominator_sum
        y_intercept = average_y - estimated_slope * average_x

        return estimated_slope, y_intercept

    except ZeroDivisionError:
        raise ValueError("you cannot divide by zero")

def predict_y(x, m, b):
    try:
        # y = mx + b
        predicted_y = (m * x) + b
        return predicted_y

    except TypeError:
        raise ValueError("all user inputs have to be rational numbers")

