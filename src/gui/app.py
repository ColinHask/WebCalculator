from flask import Flask, render_template, request
from src import logic
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    # initially render html
    return render_template('index.html')

@app.route('/calculate', methods = ['POST'])
def calculate():
    # get entry value
    entry = request.form.get('entry')

    #render template with entry value submitted
    return render_template('index.html', entry=entry)