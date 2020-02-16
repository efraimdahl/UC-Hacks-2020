from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TextEntry(FlaskForm):
    food = StringField('food', validators=[DataRequired()])
    amount = StringField('amount', validators=[DataRequired()])
    submit = SubmitField('Enter')
