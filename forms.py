from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class IntroForm(FlaskForm):
    email = StringField('Email Address (see notes below)', validators=[DataRequired()])
    blurb = TextAreaField('Tell us a little about your background or interest in STEM as it relates to socialism, we do not need any personally identifying information.', validators=[DataRequired()])
    submit = SubmitField('Submit')
