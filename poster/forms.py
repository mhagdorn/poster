from flask_wtf import FlaskForm
from wtforms import IntegerField, validators


class DataForm(FlaskForm):
    years = IntegerField(
        label="years",
        validators=[validators.required(),
                    validators.NumberRange(0, 100)])

    income = IntegerField(
        label="income",
        validators=[validators.required(),
                    validators.NumberRange(0, 1000000)])
