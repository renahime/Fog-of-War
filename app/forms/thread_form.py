from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.models import Thread, User


class ThreadForm(FlaskForm):
    subject = StringField('Subject', validators=[Length(max=255, message="Subject name is too long!"), DataRequired()])
    text = TextAreaField('Text Box', validators=[DataRequired()])
