# This is a simple Flask application that handles user login.
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data
users = {"test@test.com": "password123"}

@app.route('/', methods=['GET', 'POST'])
#Login route that handles both GET and POST requests
def login():
    error = None
    login_success = False
    # If the request method is POST, check the credentials
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password_input']
        if username in users and users[username] == password:
            login_success = True
            # Redirect to the main page if login is successful
            return redirect(url_for('main_page'))
        else:
            error = "Invalid email or password. Please try again."
    return render_template('index.html', error=error)

# Route for the main page after successful login
@app.route('/main')
def main_page():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)