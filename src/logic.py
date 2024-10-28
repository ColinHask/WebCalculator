import math

def calculate_mean(number_list):
    if len(number_list) == 0:
        raise ValueError
    else:
        count = 0
        ans = 0
        for number in number_list:
            count = count+1
            ans += number
        return ans / count

def calculate_standard_deviation(number_list):
    if len(number_list) == 0:
        raise ValueError
    else:
        mean = sum(number_list) / len(number_list)  # mean
        var = sum(pow(x - mean, 2) for x in number_list) / len(number_list)  # variance
        return math.sqrt(var)  # standard deviation

def calculate_z_score(value, mean, standard_deviation):
    if standard_deviation == 0:
        raise ValueError
    else:
        result = (value - mean)/standard_deviation
        return result

def compute_single_linear_regression(xy_list):
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

def predict_y_from_linear_regression(x,m,b):
    #y = mx + b
    predicted_y = (m*x) + b
    return predicted_y


