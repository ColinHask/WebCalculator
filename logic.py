def calculate_mean(number_list):
    count = 0
    ans = 0
    for number in number_list:
        count = count+1
        ans += number
    return ans / count
