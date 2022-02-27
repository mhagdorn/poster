from flask_wtf import FlaskForm
from wtforms import IntegerField, validators


class DataForm(FlaskForm):
    spinalPoint = IntegerField(
        label="spinal point",
        validators=[validators.required(),
                    validators.NumberRange(1, 66)])
