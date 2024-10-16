from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'The web dev part might not be that hard'

if __name__ == '__main__':
    app.run(debug=True)
