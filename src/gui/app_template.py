from flask import Flask, render_template, request
#import Logic

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('indexTemplate.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    number1 = request.form.get('number1')
    number2 = request.form.get('number2')
    operation = request.form.get('operation')

    # Debugging: Print the operation to console
    print(f"Operation selected: {operation}")

    try:
        num1 = float(number1)
        num2 = float(number2)
    except ValueError:
        error_message = "Please enter valid numbers."
        return render_template('indexTemplate.html', result=error_message)

    if operation == 'Add':
        result = num1 + num2
    elif operation == 'Subtract':
        result = num1 - num2
    elif operation == 'Multiply':
        result = num1 * num2
    elif operation == 'Divide':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Cannot divide by zero."
    else:
        result = "Invalid operation."

    return render_template('indexTemplate.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
