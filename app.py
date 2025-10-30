"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import csv
from datetime import datetime
from typing import List, Dict, Set, Union


from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from utils.libraries import open_movie_database, open_movie_genres, open_spoken_languages, open_release_dates, open_runtimes, open_scores
from utils.data_value_type_editor import correct_value_type
from filtering.filter_selector import filter_selection
from filtering.filter_executor import filter_movies
from utils.weight_calculations import min_max_value, factor_weight, calc_movie_score_weight
from classes.temp_user import temp_user
from classes.virtual_room import virtual_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app





@app.route('/', methods = ["GET", "POST"])
def main():
    
    movie_genres = open_movie_genres() # Open movie geners list

    spoken_languages = open_spoken_languages() # Open spoken languages list

    runtimes = open_runtimes() # Open runtimes list

    scores = open_scores() # Open scores list

    release_dates = open_release_dates() # Open release dates list

    movie_database = open_movie_database() # Open movie database

    #corrected_values_movies = correct_value_type(movie_database) # Correct the values of some data in the movie database







    """Renders a sample page."""
    return render_template('index.html', template_form = movie_genres, spoken_languages = spoken_languages, scores = scores, runtimes = runtimes, release_dates = release_dates)







if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)
