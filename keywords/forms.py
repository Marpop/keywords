from flask_wtf import FlaskForm
from wtforms import StringField, validators


class URLForm(FlaskForm):
    url = StringField("URL:", validators=[validators.URL(), validators.DataRequired()])
