# Flask Demo Application
# This is a simple Flask application to demonstrate the basics of using Flask.
# Flask is a lightweight web application framework written in Python.
# It allows you to build web applications quickly and with a minimal amount of code.

# First, you need to install Flask.
# You can install Flask using pip, the Python package manager.
# Open your command prompt or terminal and run:
# pip install flask

# Import the Flask class from the flask module
from flask import Flask, render_template

# Create an instance of the Flask class.
# __name__ is a special variable that gets as value the string "__main__" when you’re executing the script.
app = Flask(__name__)

# Use the route() decorator to tell Flask what URL should trigger the function.
@app.route('/')
def hello_world():
    # This function returns the message we want to display in the user's browser.
    return 'Hello, World! Welcome to your first Flask app.'

# Let's add another route.
@app.route('/about')
def about():
    # This route returns a simple string.
    return 'This is the about page.'

# Using variables in routes.
# You can use angle brackets to add variable parts to the URL.
@app.route('/user/<username>')
def show_user_profile(username):
    # Show the user profile for that user
    return f'User: {username}'

# Let's use an integer variable in the route.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Show the post with the given id
    return f'Post ID: {post_id}'

# Rendering templates.
# Templates are files that contain static data as well as placeholders for dynamic data.
# Let's create a route that renders an HTML template.
@app.route('/hello/<name>')
def hello(name):
    # The render_template function looks for templates in the templates folder.
    return render_template('hello.html', name=name)

# To run the application, use the following code.
if __name__ == '__main__':
    # The run() method runs the application on a local development server.
    # The debug=True flag will reload the server automatically when you make changes,
    # and will provide helpful debugging information.
    app.run(debug=True)

# Save this file as app.py
# To run the application, open your terminal and navigate to the directory containing app.py
# Then run:
# python app.py
# Open your web browser and go to http://127.0.0.1:5000/
# You should see "Hello, World! Welcome to your first Flask app." displayed.

# Try accessing the following URLs:
# http://127.0.0.1:5000/about
# http://127.0.0.1:5000/user/JohnDoe
# http://127.0.0.1:5000/post/123
# http://127.0.0.1:5000/hello/YourName
