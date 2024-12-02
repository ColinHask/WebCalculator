from flask import Flask, render_template, request

#import calculator_logic functionalities from calculator_logic folder
from src.calculator_logic import regression, statistics
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    # initially render html
    result_default = "Enter values below, then select an operation"
    return render_template('index.html', result = result_default, error=False)

@app.route('/calculate', methods = ['POST'])
def calculate():

    #result variable is the exact output to user
    #used for the result of the operation OR the error message to the user
    result = "Enter values below, then select an operation"

    #used by HTML to render error state visuals
    #default state false
    error_state = False

    #header for result / message board
    msg_header = ""

    #get needed values from html
    entry = request.form.get('entry')
    operation = request.form.get('operation')

    # Debugging: Print the operation to console
    print(f"Operation selected: {operation}")


    # clear operation check before input handling
    if operation == "clear":
        return render_template('index.html', result = result, error = False)

    #try catch for input checking
    try:

        #remove any spaces from input
        entry.replace(" ", "")

        if operation == "Single Linear Regression Prediction" or operation == "Z-Score":
            # split entry into list by commas
            entry = entry.split(',')
            if len(entry) > 3:
                raise Exception("too many values")
        else:
            # split entry into list by new line
            entry = entry.split("\n")

        if operation == "Single Linear Regression Formula:":
            count = 0
            # convert a list of strings num,num ex:"34,45" into a list of floats
            for i in entry:
                # split into list (2 strings)
                entry[count] = i.split(",")
                # convert items to floats
                (entry[count])[0] = float((entry[count])[0])
                (entry[count])[1] = float((entry[count])[1])
                if len(entry[count]) > 2:
                    #invalid input
                    print("ordered pair length error found")
                    raise Exception("too many values")
                count += 1

        else:
                # turn list into int
                count = 0
                for i in entry:
                    entry[count] = float(i)
                    count += 1



        #DEBUGGING PRINT
        print("entry: "+str(entry))

        if operation == 'Mean':
            """
            Takes a list of any real number elements and then calculates the mean by adding all the elements and dividing by
            the number of them
            """
            try:
                result = statistics.mean(entry)
            except Exception as e:
                error_state = True
                msg_header = "Calculation Error"
                result = "Invalid entry, " + str(e)


        elif operation == 'Sample Standard Deviation':
            """
            Intakes a list of any numbers and calculates the mean from the mean function.
            The mean is then used in the variance function. Finally, the square root of the variance
            give the standard deviation
            """
            try:
                result = statistics.sample_standard_deviation(entry)
            except Exception as e:
                error_state = True
                msg_header = "Calculation Error"
                result = "Invalid entry, " + str(e)

        elif operation == 'Population Standard Deviation':
            """
            Intakes a list of any numbers and calculates the mean from the mean function.
            The mean is then used in the variance function. Finally, the square root of the variance
            give the standard deviation
            """
            try:
                result = statistics.population_standard_deviation(entry)
            except Exception as e:
                error_state = True
                msg_header = "Calculation Error"
                result = "Invalid entry, " + str(e)

        elif operation == 'Z-Score':
            """
            Takes three inputs value, average (i.e., mean), and variation (i.e., standard deviation) and then returns the z score.
            Chose a different synonym for mean and standard deviation due to methods having similar names
            """
            try:
                # set variables for method call
                value = entry[0]
                average = entry[1]
                variation = entry[2]
                result = statistics.z_score(value, average, variation)
            except Exception as e:
                error_state = True
                result = "Invalid entry " + str(e)

        elif operation == 'Single Linear Regression Formula:':
            """
            intakes a list of number pairs (e.g., [(x1,y1),...,(xn,yn)]) and returns the estimated slope and
            then uses the calculations of that slope to return the predicted y intercept
            """
            try:
                result = regression.linear_regression(entry)
            except Exception as e:
                error_state = True
                msg_header = "Calculation Error"
                result = "Invalid entry, " + str(e)

        elif operation == 'Single Linear Regression Prediction':
            """
            intakes three variables which I purposely named x, m and b since this calculation using form y = mx + b standard
            linear polynomial equation. Finally, it returns the value of the function (i.e., y) using the slope, the x value
            and the y intercept.
            """
            try:
                #set variables for method call
                x = entry[0]
                m = entry[1]
                b = entry[2]
                result = regression.predict_y(x, m, b)

            except Exception as e:
                error_state = True
                msg_header = "Calculation Error"
                result = "Invalid entry, " + str(e)

        else:
            # should never run (invalid operation selected)
            # DEBUGGING PRINT
            error_state = True
            print("Invalid operation")
            msg_header = "Invalid input"
            result = "Invalid operation"

    # executes if error occurs due to user input
    except Exception as e:
        #DEBUGGING PRINT
        print(e)

        error_state = True
        if operation == "Mean":
            result = "Mean format is: individual values on each line"
        elif operation == "Population Standard Deviation" or operation == "Sample Standard Deviation":
            result = "Standard Deviation format is: individual values on each line"
        elif operation == "Z-Score":
            result = "Z-Score format is: \"value, mean, standard deviation\" values on one line (seperated by commas)"
        elif operation == "Single Linear Regression Formula:":
            result = "Linear regression format is: one ordered pair on each line. Ex: 1,2"
        elif operation == "Single Linear Regression Prediction":
            result = "Predict Y format is: \"m,x,b\" values on one line (seperated by commas)"
        else:
            result = "Invalid entry, please try again"


        msg_header = "Invalid input"
        # DEBUGGING PRINT
        print("Invalid entry: " + str(entry))

    #testing
    # DEBUGGING PRINT
    print("result: " + str(result))

    if not error_state:
        msg_header = operation



    #render template with entry and result value submitted
    return render_template('index.html', msgHeader=msg_header, result=result, error=error_state)