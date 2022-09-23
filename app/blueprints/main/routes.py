from . import bp as app
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.main.models import Car
from app import db


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/car')
def create_car():
    car_make = request.form['make']
    car_model = request.form['model']
    car_year = request.form['year']
    car_color = request.form['color']
    car_price = request.form['price']
    # print(car_make,car_model,car_year,car_color,car_price)
    new_car = Car(make=car_make, model=car_model, year=car_year, color=car_color, price=car_price, user_id=1)

    db.session.add(new_car)
    db.session.commit()

    flash('Car added succesfully', 'success')
    return redirect(url_for('main.home'))