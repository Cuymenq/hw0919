from . import bp as app
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.main.models import Car
from app import db


logged_in_user=1
@app.route('/')
def home():
    cars = Car.query.all()
    return render_template('home.html', cars=cars)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/car', methods=['POST'])
def create_car():
    car_make = request.form['Make']
    car_model = request.form['Model']
    car_year = request.form['Year']
    car_color = request.form['Color']
    car_price = request.form['Price']
    # print(car_make,car_model,car_year,car_color,car_price)
    new_car = Car(make=car_make, model=car_model, year=car_year, color=car_color, price=car_price, user_id=1)

    db.session.add(new_car)
    db.session.commit()

    flash('Car added succesfully', 'success')
    return redirect(url_for('main.home'))
