from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.login_model import Volunteer
import os
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# this is where we will import our models and connect them to our routes

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/contact')
def contact():
    api_key = os.environ.get('FLASK_APP_API_KEY')
    return render_template('contact.html', api_key=api_key)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html')

@app.route('/volunteer_submit', methods=['POST'])
def volunteer_submit():
    data ={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'phone': request.form['phone']
    }
    print(request.form)
    Volunteer.save(data)
    return redirect('/')

@app.route('/photo')
def photo():
    return render_template('photo_gallery.html')

# add login and registration routes and logic