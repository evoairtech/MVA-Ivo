from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, StringField, SubmitField
from wtforms.validators import DataRequired

class filter_form(FlaskForm):
    genres = SelectMultipleField('Genres', choices=[])  # Empty list initially
    languages = SelectMultipleField('Languages', choices=[])  # Empty list initially
    runtime = SelectMultipleField('Runtime', choices=[])  # Empty list initially
    scores = SelectMultipleField('Scores', choices=[])  # Empty list initially
    release_date = StringField('Release Year or Range (e.g. 2012-2015)', validators=[DataRequired()])
    submit = SubmitField('Apply Filters')
