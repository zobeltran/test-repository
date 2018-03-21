"""
This is the User Routes
"""
from flask import Blueprint, render_template, redirect, url_for
from app.models import Packages, HotelBookings, FlightBooking, DB
from flask_user import login_required
from datetime import datetime
from app.users import forms
from app.models import Packages
from flask_socketio import SocketIO, send

SOCKETIO = SocketIO()

MOD_USER = Blueprint('main', __name__, template_folder='templates',
                     static_folder='static', static_url_path='/%s' % __name__)


@MOD_USER.route('/user')
@login_required
def homepage():
    """ User Homepage """
    flights = FlightBooking.query.order_by(
        FlightBooking.fbooking_id.desc()).all()
    hotels = HotelBookings.query.order_by(
        HotelBookings.hbooking_id.desc()).all()
    packages = Packages.query.order_by(Packages.package_id.desc()).all()
    return render_template("homepage.html", flights=flights, hotels=hotels, packages=packages)


@MOD_USER.route('/user/createpromo', methods=['POST', 'GET'])
@login_required
def promo():
    """ Promo Creation page """
    form = forms.PackagesForm()
    if form.validate_on_submit():
        package = Packages(package_name=form.package_name.data, package_description=form.description.data,
                           package_price=form.package_price.data, package_createtime=datetime.today(), package_updated=datetime.today())
        DB.session.add(package)
        DB.session.commit()
        return redirect( url_for("main.homepage", code=307))
    print(form.errors)
    return render_template('createpackage.html', form=form)


@MOD_USER.route('/user/flightdelete/confirm/<int:fbooking_id>')
@login_required
def fdelete(fbooking_id):
    """ Flight Deletion """
    flights = FlightBooking.query.get_or_404(fbooking_id)
    DB.session.delete(flights)
    DB.session.commit()
    return redirect(url_for('main.homepage')) 


@MOD_USER.route('/user/hoteldelete/confirm/<int:hbooking_id>')
@login_required
def hdelete(hbooking_id):
    """ Flight Deletion """
    hotel = HotelBookings.query.get_or_404(hbooking_id)
    DB.session.delete(hotel)
    DB.session.commit()
    return redirect(url_for('main.homepage'))

@MOD_USER.route('/user/packagedelete/confirm/<int:package_id>')
@login_required
def pdelete(package_id):
    """ Flight Deletion """
    packages = Packages.query.get_or_404(package_id)
    DB.session.delete(packages)
    DB.session.commit()
    return redirect(url_for('main.homepage')) 

@MOD_USER.route('/user/chat')
def chat():
    @SOCKETIO.on('message')
    def handleMessage(msg):
        print('Message: ' + msg)
        send(msg, broadcast=True)
    return render_template('adminchat.html')