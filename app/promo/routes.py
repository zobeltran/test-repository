"""
This is the routes file for promo
"""
from flask import Blueprint, render_template, request, url_for, redirect
from app.models import Packages, HotelBookings, FlightBooking, DB
from app.promo import forms
from flask_socketio import SocketIO, send
import stripe

SOCKETIO = SocketIO()



MOD_PROMO = Blueprint('promo', __name__, template_folder='templates',
                      static_folder='static', static_url_path='/%s' % __name__)

pubkey = 'pk_test_GjK3GmJJ1exs60wIcgTpfggq'
secretkey = 'sk_test_RXyvP1FBgkRyCwyEBGyZeymo'

stripe.api_key = secretkey

@MOD_PROMO.route('/')
def promos():
    """ Promos """
    packages = Packages.query.order_by(Packages.package_id.desc()).all()
    return render_template("packages.html", packages=packages)


@MOD_PROMO.route('/package/<int:package_id>')
def package(package_id):
    """ Package """
    packages = Packages.query.filter_by(package_id=package_id).all()
    return render_template('getpackage.html', packages=packages, pubkey=pubkey)


@MOD_PROMO.route('/flights/confirm')
def confirmflight():
    """ Flight Confirmation """
    return render_template("flightconfirmation.html")


@MOD_PROMO.route('/bookings/confirm')
def confirmhotel():
    """ Hotel Confirmation """
    return render_template("hotelconfirmation.html")

@MOD_PROMO.route('/flights', methods=['GET', 'POST'])
def flights():
    """ Flights """
    form = forms.FlightForm()
    # print(form.errors)
    if form.validate_on_submit():
        flight = FlightBooking(fbooking_email=form.email.data, fbooking_departure=form.place_from.data,
                               fbooking_arrival=form.place_to.data, fbooking_departure_date=form.departure_date.data, fbooking_arrival_date=form.arrival_date.data,
                               fbooking_budget_range=form.budget_range.data, fbooking_head_count=form.head_count.data)
        DB.session.add(flight)
        DB.session.commit()
        return redirect(url_for("promo.confirmflight", code=307))
    print(form.errors)
    return render_template("flightbooking.html", form=form)


@MOD_PROMO.route('/bookings', methods=['GET', 'POST'])
def bookings():
    """ Bookings """
    form = forms.HotelForm()
    if form.validate_on_submit():
        hotel = HotelBookings(hbooking_email=form.email.data, hbooking_location=form.hotel_location.data, hbooking_check_in=form.check_in_date.data,
                              hbooking_check_out=form.check_out_date.data, hbooking_number_of_rooms=form.number_of_rooms.data, hbooking_budget_range=form.budget_range.data)
        DB.session.add(hotel)
        DB.session.commit()
        return redirect(url_for("promo.confirmhotel", code=307))
    print(form.errors)
    return render_template("hotelbooking.html", form=form)
  
@MOD_PROMO.route('/packagepayment/confirm')
def confirmpromo():
    """ Payment Confimation """
    return render_template("confirmpayment.html")

@MOD_PROMO.route('/packagepayment/<int:package_id>', methods=['POST'])
def pay(package_id):
    """ Payment Server Side """
    print(request.form)
    packages = Packages.query.filter_by(package_id=package_id).all()

    customer = stripe.Customer.create(
        email=request.form['stripeEmail'], source=request.form['stripeToken'])

    for items in packages:
        charge = stripe.Charge.create(
            customer=customer.id,
            amount=items.package_price * 100,
            currency="php",
            description=items.package_name
    )
    return redirect(url_for("promo.confirmpromo", code=307))

@MOD_PROMO.route('/chat')
def chat():
    @SOCKETIO.on('message')
    def handleMessage(msg):
        print('Message: ' + msg)
        send(msg, broadcast=True)
    return render_template('chat.html')