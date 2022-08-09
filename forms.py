""" Sample module docstring """
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SendEmail(FlaskForm):
    """ Sample class docstring """
    email = StringField('Your Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired(), Length(min=20, max=500)])
    submit = SubmitField('Send Email')
