from flask import Flask, render_template, request
#import logic functionalities from logic folder
from src.logic import regression, statistics
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    # initially render html
    return render_template('index.html')

@app.route('/calculate', methods = ['POST'])
def calculate():
    # get entry value
    result = ""
    #get needed values from html
    entry = request.form.get('entry')
    operation = request.form.get('operation')

    #split entry into list
    entry = entry.split("\n")


    # Debugging: Print the operation to console
    print(f"Operation selected: {operation}")

    #try catch for input checking
    try:
        if operation == "regression":
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

        if operation == 'mean':
            """
            Takes a list of any real number elements and then calculates the mean by adding all the elements and dividing by
            the number of them
            """
            try:
                result = statistics.mean(entry)
            except Exception as e:
                result = "invalid entry " + str(e)

        elif operation == 'deviation':
            """
            Intakes a list of any numbers and calculates the mean from the mean function.
            The mean is then used in the variance function. Finally, the square root of the variance
            give the standard deviation
            """
            try:
                result = statistics.standard_deviation(entry)
            except Exception as e:
                result = "invalid entry " + str(e)

        elif operation == 'zscore':
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
                result = "invalid entry " + str(e)

        elif operation == 'regression':
            """
            intakes a list of number pairs (e.g., [(x1,y1),...,(xn,yn)]) and returns the estimated slope and
            then uses the calculations of that slope to return the predicted y intercept
            """
            try:
                result = regression.linear_regression(entry)
            except Exception as e:
                result = "invalid entry " + str(e)

        elif operation == 'predict':
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
                result = "invalid entry " + str(e)
        else:
            # should never run (invalid operation selected)
            # DEBUGGING PRINT
            print("Invalid operation")
            result = "Invalid operation (this shouldn't be possible)"

    except Exception as e:
        result = "invalid entry, please enter values as numbers"
        # DEBUGGING PRINT
        print("invalid entry: " + str(entry))

    #testing
    # DEBUGGING PRINT
    print("result: " + str(result))

    #render template with entry and result value submitted
    return render_template('index.html', entry=entry,result=result)