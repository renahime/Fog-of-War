from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError, Length, URL
from flask_wtf.file import FileField, FileAllowed, FileRequired

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}


class ImageForm(FlaskForm):
  image = FileField("image", validators=[FileAllowed(list(ALLOWED_EXTENSIONS)), FileRequired()])
