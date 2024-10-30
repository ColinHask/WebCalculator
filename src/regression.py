import math


def linear_regression(xy_list):
    number_of_pairs = len(xy_list)

    total_x = 0
    for i in xy_list:
        total_x += i[0]
    average_x = total_x / number_of_pairs

    total_y = 0
    for i in xy_list:
        total_y += i[1]
    average_y = total_y / number_of_pairs

    xy_difference_product = 0
    x_difference_squared = 0
    for i in xy_list:
        xy_difference_product += (i[0] - average_x) * (i[1] - average_y)
        x_difference_squared += (i[0] - average_x) ** 2
    m = xy_difference_product / x_difference_squared

    b = average_y - m * average_x

    print(f"y = {m}x + {b}")


def predict_y(x, m, b):
    # y = mx + b
    predicted_y = (m * x) + b
    return predicted_y
