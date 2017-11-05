from wtforms import Form, FloatField, validators

class InputForm(Form):
    btc = FloatField(
        label='BtcVal', default=1.0,
        validators=[validators.InputRequired()])
    inr = FloatField(
        label='InrVal', default=1.0,
        validators=[validators.InputRequired()])