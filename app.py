from flask import Flask, render_template, request, redirect,jsonify, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import os
import pickle
import re

app = Flask(__name__)

app.secret_key = 'xyzsdfg'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hdps'

mysql = MySQL(app)








@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password,))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('user.html', mesage=mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage=mesage)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('home'))


@app.route('/Login')
def Login():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/Register')
def Register():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('name', None)
    session.pop('email', None)
    session.pop('password', None)
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email,))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s)', (userName, email, password,))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage=mesage)


# Define the path to the model file
model_file_path = 'model.pkl1'


try:
    model = pickle.load(open(model_file_path, 'rb'))
except FileNotFoundError:
    # Handle the case where the file is not found
    model = None
    print(f"Error: The file '{model_file_path}' was not found.")
except Exception as e:
    # Handle other exceptions that may occur during file opening
    model = None
    print(f"Error: An exception occurred while opening '{model_file_path}': {str(e)}")




@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        # Handle the case where the model is not available
        return jsonify({'error': 'Model not available'})
    # Get input data from POST request
    age = int(request.form.get('Age'))
    sex = int(request.form.get('sex'))
    chestpaintypes = int(request.form.get('chestPainTypes'))
    trestbps = int(request.form.get('trestBps'))
    serumcholesterol = int(request.form.get('SerumCholesterol'))
    fastingbloodsugar = int(request.form.get('FastingBloodSugar'))
    ecgresults = int(request.form.get('ecg_results'))
    maximumheartrate = int(request.form.get('MaximumHeartRate'))
    exerciseangina = int(request.form.get('exercise_angina'))
    stdepression = float(request.form.get('stDepression'))

    stslope = int(request.form.get('st_slope'))
    majorvessels = int(request.form.get('major_vessels'))
    thalassemia = int(request.form.get('thalassemia'))

    # Create input array for prediction
    input_query = np.array([[age, sex, chestpaintypes, trestbps, serumcholesterol, fastingbloodsugar,

    ecgresults,maximumheartrate, exerciseangina, stdepression, stslope, majorvessels, thalassemia]])

    # Make prediction
    prediction = model.predict(input_query)

    if isinstance(prediction, (list, np.ndarray)) and len(prediction) > 0:
        if prediction[0] == 0:
            result = 'The Person does not have Heart Disease'
        else:
            result = 'The Person has Heart Disease'
    else:
        result = 'Invalid prediction data'

    return render_template('user.html', result=result)










if __name__ == '__main__':
    app.run(debug=True)







if __name__ == "__main__":
    app.run(debug=True)