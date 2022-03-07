from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, validators


class DataForm(FlaskForm):
    start_year = IntegerField(
        label="start year",
        default=2009,
        validators=[validators.InputRequired(),
                    validators.NumberRange(2009, 2020)])

    income = IntegerField(
        label="income",
        default=36000,
        validators=[validators.InputRequired(),
                    validators.NumberRange(0, 1000000)])


class EmailForm(FlaskForm):
    email = StringField("email",
                        [validators.InputRequired(),
                         validators.Email(
                             "This field requires a valid email address")])
