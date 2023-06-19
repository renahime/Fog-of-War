from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.models import Thread, User


class EditThreadForm(FlaskForm):
    subject = StringField('subject', validators=[Length(max=255, message="Subject name is too long!")])
    text = TextAreaField('text')
