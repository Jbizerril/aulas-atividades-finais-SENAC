from flask import Blueprint, render_template, request, redirect, url_for
from models.bike_model import Bike
from services.bike_service import BikeService

bike_bp = Blueprint('bike', __name__)
bike_service = BikeService()

@bike_bp.route('/')
def index():
    bikes = bike_service.bikes
    return render_template('index.html', bikes=bikes)

@bike_bp.route('/add', methods=['POST'])
def add_bike():
    model = request.form['model']
    category = request.form['category']
    price = float(request.form['price'])
    new_bike = Bike(model, category, price)
    result = bike_service.add_bike(new_bike)
    return redirect(url_for('bike.index'))

@bike_bp.route('/sell/<model>')
def sell_bike(model):
    result = bike_service.mark_as_sold(model)
    return redirect(url_for('bike.index'))
