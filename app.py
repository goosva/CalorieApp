#import flask and create instance of flask object
from flask import Flask, render_template, url_for, redirect, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
#This tells our app where the database is located
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'
#starts the databse
db = SQLAlchemy(app)

class user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(20), nullable = False)
    password_hash = db.Column(db.Integer, default=0)
    data_created = db.Column(db.DateTime, default=datetime.now)
    last_login = db.Column(db.DateTime, default=datetime.now)

#function that returns content
@app.route("/") #decorator to map URL route / to function
def index():
    return render_template('index.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))
    
@app.route('/success')
def success():
    return 'logged in successfully'

if __name__ == "__main__":
    app.run(debug=True)
