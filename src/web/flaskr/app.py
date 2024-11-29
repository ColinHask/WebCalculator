from django.db.models.expressions import result
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

        if operation == "Single Linear Regression Prediction":
            # split entry into list by commas
            entry = entry.split(',')
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
                result = "invalid entry " + str(e)

        elif operation == 'Population Standard Deviation':
            """
            Intakes a list of any numbers and calculates the mean from the mean function.
            The mean is then used in the variance function. Finally, the square root of the variance
            give the standard deviation
            """
            try:
                result = statistics.standard_deviation(entry)
            except Exception as e:
                error_state = True
                result = "invalid entry " + str(e)

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
                result = "invalid entry " + str(e)

        elif operation == 'Single Linear Regression Formula:':
            """
            intakes a list of number pairs (e.g., [(x1,y1),...,(xn,yn)]) and returns the estimated slope and
            then uses the calculations of that slope to return the predicted y intercept
            """
            try:
                result = regression.linear_regression(entry)
            except Exception as e:
                error_state = True
                result = "invalid entry " + str(e)

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
                result = "invalid entry " + str(e)

        else:
            # should never run (invalid operation selected)
            # DEBUGGING PRINT
            error_state = True
            print("Invalid operation")
            result = "Invalid operation (this shouldn't be possible)"

    # executes if error occurs due to user input
    except Exception as e:
        error_state = True
        result = "invalid entry, please enter values as numbers"
        # DEBUGGING PRINT
        print("invalid entry: " + str(entry))

    #testing
    # DEBUGGING PRINT
    print("result: " + str(result))

    if error_state:
        msg_header = "Invalid Input"
    else:
        msg_header = operation



    #render template with entry and result value submitted
    return render_template('index.html', msgHeader=msg_header, result=result, error=error_state)