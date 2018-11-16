from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class IntroForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired()])
    blurb = TextAreaField('Tell Us About Yourself!', validators=[DataRequired()])
    submit = SubmitField('Submit')
