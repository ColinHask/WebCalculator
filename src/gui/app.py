from flask import Flask, render_template, request
from shapely.ops import substring

from src import logic
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    # initially render html
    return render_template('index.html')

@app.route('/calculate', methods = ['POST'])
def calculate():
    # get entry value
    result = ""
    entry = request.form.get('entry')
    operation = request.form.get('operation')

    #split entry into list
    entry = entry.split("\n")
    count = 0

    #try catch for input checking
    try:
        #turn list into int
        for i in entry:
            entry[count] = int(i)
            count += 1

        #DEBUGGING PRINT
        print(entry)

        if operation == 'mean':
            try:
                result = logic.calculate_mean(entry)
            except Exception as e:
                result = "invalid entry" + str(e)
        elif operation == 'deviation':
            try:
                result = logic.calculate_standard_deviation(entry)
            except Exception as e:
                result = "invalid entry" + str(e)
        elif operation == 'zscore':
            try:
                # set variables for method call
                value = entry[0]
                mean = entry[1]
                stand = entry[2]
                result = logic.calculate_z_score(value, mean, stand)
            except Exception as e:
                result = "invalid entry" + str(e)
        elif operation == 'regression':
            try:
                result = logic.compute_single_linear_regression(entry)
            except Exception as e:
                result = "invalid entry" + str(e)
        elif operation == 'predict':
            try:
                #set variables for method call
                one = entry[0]
                two = entry[1]
                three = entry[2]
                result = logic.predict_y_from_linear_regression(one, two, three)

            except Exception as e:
                result = "invalid entry" + str(e)
        else:
            # should never run (invalid operation selected)
            # DEBUGGING PRINT
            print("shit didnt work")
            result = "how did we get here"
    except Exception as e:
        result = "invalid entry, please enter values as numbers"


    #testing
    # DEBUGGING PRINT
    print(result)
    # Debugging: Print the operation to console
    print(f"Operation selected: {operation}")


    #render template with entry and result value submitted
    return render_template('index.html', entry=entry,result=result)