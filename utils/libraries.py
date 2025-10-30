import csv
from typing import List, Dict, Set, Union

def open_movie_genres() -> List[str]:
    """
    Open the genres file turning it from a csv file into a an object that contains the whole table of movie genres as a list
    """
    print("Loading genres...")
    movie_genres = []
    with open("movie_genres.csv", encoding='utf-8') as genres_file: # Open the file with the database
        genres_reader = csv.reader(genres_file) # read the database file
        for row in genres_reader:
            for genre in row:                
                movie_genres.append(genre)
    print("Genres Loaded")
    return movie_genres


def open_spoken_languages() -> List[str]:
    """
    Open the genres file turning it from a csv file into a an object that contains the whole table of movie genres as a list
    """
    print("Loading languages...")
    spoken_languages = []
    with open("spoken_languages.csv", encoding='utf-8') as languages_file: # Open the file with the database
        languages_reader = csv.reader(languages_file) # read the database file
        for row in languages_reader:
            for language in row:
                spoken_languages.append(language)
    print("Languages Loaded")
    return spoken_languages


def open_scores() -> List[str]:
    """
    Open the genres file turning it from a csv file into a an object that contains the whole table of movie genres as a list
    """
    print("Loading scores...")
    scores = []
    with open("scores.csv", encoding='utf-8') as scores_file: # Open the file with the database
        scores_reader = csv.reader(scores_file) # read the database file
        for row in scores_reader:
            for score in row:                
                scores.append(score)
    print("Scores Loaded")
    return scores


def open_runtimes() -> List[str]:
    """
    Open the genres file turning it from a csv file into a an object that contains the whole table of movie genres as a list
    """
    print("Loading runtimes...")
    runtimes = []
    with open("runtimes.csv", encoding='utf-8') as runtimes_file: # Open the file with the database
        runtimes_reader = csv.reader(runtimes_file) # read the database file
        for row in runtimes_reader:
            for runtime in row:                
                runtimes.append(runtime)
    print("Runtimes Loaded")
    return runtimes


def open_release_dates() -> List[str]:
    """
    Open the genres file turning it from a csv file into a an object that contains the whole table of movie genres as a list
    """
    print("Loading release dates...")
    release_dates = []
    with open("release_dates.csv", encoding='utf-8') as release_date_file: # Open the file with the database
        release_date_reader = csv.reader(release_date_file) # read the database file
        for row in release_date_reader:
            for release_date in row:                
                release_dates.append(int(release_date))
    sorted_release_dates = sorted(release_dates, reverse=True)
    print("Release Dates Loaded")
    return sorted_release_dates


def open_movie_database() -> Dict[str, str]:
    """
    Open the database turning it from a csv file into a an object that contains the whole database as a list of dictionaries
    """
    print("Loading movie database...")
    movie_database = []
    with open("TMDB_movie_dataset_v11.csv", encoding='utf-8') as movie_file: # Open the file with the database
        movie_reader = csv.DictReader(movie_file) # read the database file
        for row in list(movie_reader):
            movie_database.append(row)
    print("Database Loaded")
    return movie_database