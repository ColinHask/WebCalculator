import math

###############################################################################

def mean(number_list):
    """
    Takes a list of any real number elements and then calculates the mean by
    adding all the elements and dividing by the number of them
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

def sample_standard_deviation(number_list):
    """
    Intakes a list of any numbers and calculates the sample standard deviation.
    Instead of using n like with population deviation, variance is calculated
    using n-1.
    """
    # if statement that accounts for 0 and 1 since n-1 results in negative
    # values
    if len(number_list) < 2:
        raise ValueError("At least two data points are needed for sample"
                         " standard deviation.")

    avg = mean(number_list)

    total = 0
    for i in number_list:
        total += (i - avg) ** 2
    variance = (1 / (len(number_list) - 1)) * total

    # square root of variance is deviation according to formula
    sample_deviation = math.sqrt(variance)

    return sample_deviation

def population_standard_deviation(number_list):
    """
    Intakes a list of any numbers and calculates the mean from the mean
    function. The mean is then used in the variance function. Finally, the
    square root of the variance give the standard deviation
    """
    # checking for empty list condition
    if len(number_list) == 0:
        raise ValueError

    else:
        # using mean function defined above and then naming the variable
        # avg for clarity
        avg = mean(number_list)
        total = 0
        for i in number_list:
            total += (i - avg) ** 2
        variance = (1 / len(number_list)) * total

        # square root of variance is deviation according to formula
        population_deviation = math.sqrt(variance)

        return population_deviation


def z_score(value, average, variation):
    """
    Takes three inputs value, average (i.e., mean), and variation
    (i.e., standard deviation) and then returns the z score. Chose a
    different synonym for mean and standard deviation due to methods
    having similar names
    """
    if variation == 0:
        raise ValueError
    else:
        result = (value - average) / variation
        return result
