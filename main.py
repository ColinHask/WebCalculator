#   The goal for single linear regression is to obtain an equation of the form y = mx + b
#   To do this I need to calculate 'm'(i.e., slope) and 'b' (i.e., the y-intercept)


#   Obviously the list here is just for example that I used from our professor's github account
#   In reality when the user enters the (x,y) pairs, they click a button that will then enter
#   their values in a list like below. We might also need to check for user errors like missing
#   commas too large numbers different data conflicts etc...
user_xy_values = [(1.47, 52.21), (1.5, 53.12), (1.52, 54.48), (1.55, 55.84), (1.57, 57.2), (1.6, 58.57), (1.63, 59.93),
                  (1.65, 61.29), (1.68, 63.11), (1.7, 64.47), (1.73, 66.28), (1.75, 68.1), (1.78, 69.92), (1.8, 72.19),
                  (1.83, 74.46,)]

#   need to get the number of pairs the user gives. This will be the first thing calculated
#   when the user presses the "single linear regression button"
number_of_pairs = len(user_xy_values)

#   getting the average of the x's in the (x,y) pairs
total_x = 0
for i in user_xy_values:
    total_x += i[0]
average_x = total_x/number_of_pairs

#   getting the average of the y's in the (x,y) pairs
total_y = 0
for i in user_xy_values:
    total_y += i[1]
average_y = total_y/number_of_pairs

#   calculating slope 'm'   = sigma (x - avgx)(y - avgy) / sigma (x - avgx)^2
xy_difference_product = 0
x_difference_squared = 0
for i in user_xy_values:
    xy_difference_product += (i[0] - average_x)*(i[1] - average_y)
    x_difference_squared += (i[0] - average_x)**2
m = xy_difference_product / x_difference_squared

#   the y-intercept is a fairly simple equation
b = average_y - m * average_x

print(f"y = {m}x + {b}")




