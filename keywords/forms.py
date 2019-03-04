from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class URLForm(FlaskForm):
    url = StringField("URL:", validators=[validators.URL(), validators.DataRequired()])
    submit_button = SubmitField("Submit")
