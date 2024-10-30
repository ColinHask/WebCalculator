import math


def mean(number_list):
    if len(number_list) == 0:
        raise ValueError
    else:
        count = 0
        ans = 0
        for number in number_list:
            count = count + 1
            ans += number
        return ans / count


def standard_deviation(number_list):
    if len(number_list) == 0:
        raise ValueError
    else:
        mean = sum(number_list) / len(number_list)  # mean
        var = sum(pow(x - mean, 2) for x in number_list) / len(number_list)  # variance
        return math.sqrt(var)  # standard deviation


def z_score(value, mean, standard_deviation):
    if standard_deviation == 0:
        raise ValueError
    else:
        result = (value - mean) / standard_deviation
        return result
