"""
Form Class for Promo Modules
"""

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Length, Email
from wtforms.fields.html5 import DateField


class FlightForm(FlaskForm):
    """
    Form Class for Flights

    email           =   Email
    place_from      =   String
    place_to        =   String
    departure_date  =   Date
    arrival_date    =   Date
    budget_range    =   Float
    head_count      =   Integer
    """

    email = StringField('Email Address',
                        validators=[InputRequired(message='Please insert an Email Address'),
                                    Email(
                                        message='Please input a valid Email Address'),
                                    Length(max=100)])
    place_from = StringField('Departure Location',
                             validators=[InputRequired(message='Please insert a Departure Location'),
                                         Length(max=100)])
    place_to = StringField('Arrival Location',
                           validators=[InputRequired(message='Please insert an Arrival Location'),
                                       Length(max=100)])
    departure_date = DateField('Departure Date',
                               validators=[InputRequired(message='Please enter a Departure Date')])
    arrival_date = DateField('Arrival Date',
                             validators=[InputRequired(message='Please enter an Arrival Date')])
    budget_range = IntegerField('Budget Range',
                              validators=[InputRequired(message='Please enter a Budget Range')])
    head_count = IntegerField('Head Count',
                              validators=[InputRequired(message='Please enter the head count')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


class HotelForm(FlaskForm):
    """
    Form Class for Hotels.

    Email           =   Email
    Hotel Location  =   String
    Check in Date   =   Date
    Check out Date  =   Date
    Number of Rooms =   Integer
    Budget Range    =   Float
    """
    email = StringField('Email Address',
                        validators=[DataRequired('Please insert an Email Address'),
                                    Email(
                                        message='Please insert a valid Email Address'),
                                    Length(max=100)])
    hotel_location = StringField('Hotel Location',
                                 [DataRequired('Please insert a location for your Hotel'),
                                  Length(max=100)])
    check_in_date = DateField('Check in Date',
                              [DataRequired('Please enter a Check in Date')])
    check_out_date = DateField('Check out Date',
                               [DataRequired('Please enter a Check out Date')])
    number_of_rooms = IntegerField('Number of Rooms',
                                   [DataRequired('Please Enter number of Rooms needed')])
    budget_range = IntegerField('Budget Range',
                              [DataRequired('Please enter a Budget Range')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')
