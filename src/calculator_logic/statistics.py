import math


def mean(number_list):
    """
    Takes a list of any real number elements and then calculates the mean by adding all the elements and dividing by
    the number of them
    """

    # checking for empty list condition

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
    """
    Intakes a list of any numbers and calculates the mean from the mean function.
    The mean is then used in the variance function. Finally, the square root of the variance
    give the standard deviation
    """
    # checking for empty list condition
    if len(number_list) == 0:
        raise ValueError
    else:
        # using mean function defined above and then naming the variable avg for clarity
        avg = mean(number_list)
        total = 0
        for i in number_list:
            total += (i - avg) ** 2
        variance = (1 / len(number_list)) * total

        # square root of variance is deviation according to formula
        deviation = math.sqrt(variance)

        return deviation


def z_score(value, average, variation):
    """
    Takes three inputs value, average (i.e., mean), and variation (i.e., standard deviation) and then returns the z score.
    Chose a different synonym for mean and standard deviation due to methods having similar names
    """
    if standard_deviation == 0:
        raise ValueError
    else:
        result = (value - average) / variation
        return result
