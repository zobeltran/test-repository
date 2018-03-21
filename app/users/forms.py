"""
User Module Forms
"""

from flask_user.forms import RegisterForm
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length


class MyRegisterForm(RegisterForm):
    first_name = StringField('First name', validators=[
                             DataRequired('First name is required')])
    last_name = StringField('Last name',  validators=[
                            DataRequired('Last name is required')])


class PackagesForm(FlaskForm):
    """
    Form Class for Packages.

    PackageName     =   String
    Description  =   String
    PackagePrice   =   Float
    """
    package_name = StringField('Package Name',
                        validators=[DataRequired('Please insert an Package Name'),
                                    Length(max=100)])
    description = TextAreaField('Description',
                                 [DataRequired('Please insert a Description')])
    package_price = IntegerField('Price',
                               [DataRequired('Please enter a Package Price')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')
