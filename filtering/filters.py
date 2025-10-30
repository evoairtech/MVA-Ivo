from typing import List, Dict, Set, Union
from datetime import datetime
from utils.data_value_type_editor import correct_value_type
from utils.libraries import open_movie_genres, open_spoken_languages


# Genre filter
def genre_filter(movie_database, movie_genres) -> Dict[str, str]:
    """
    The user chooses what genres they are intersted in, if they want all genres found in the movies
    and what genres they are not intereted in.
    The functions checks if the input genres are properly spelled out (this is done by being found in a list of movie genres).
    If there are multiple genres the function ofers a choice if all genres should be found in the movies or any genre is okay.
    """

    print('Genre filter start')
    chosen_genre = input(str('\nInput chosen genre/s: ')).lower()
    genre_filtering_option = ''
    if ',' in chosen_genre:
        genre_filtering_option = input(str('Would you like to: \na) Match all selected genres \nb) Match any selected genres \nAnswer: ')).lower()
    negative_genre = input(str('Input genre/s that you don\'t wish to see: ')).lower()

    print('Genre: ', chosen_genre)
    print('Negative: ', negative_genre)

    chosen_genres_list = [genre.strip() for genre in chosen_genre.split(',')]
    negative_genres_list = [genre.strip() for genre in negative_genre.split(',')]

    print('Genre list: ', chosen_genres_list)
    print('Negative list: ', negative_genres_list)

    filtered_movies = []

    for dictionary in movie_database:    
        if dictionary['genres']:        
            dictionary_genres_lower = [genre.strip().lower() for genre in dictionary['genres'].split(",")]

            if any(genre in negative_genres_list for genre in dictionary_genres_lower):
                continue

            if genre_filtering_option == 'a':  # Match all selected genres
                if all(genre in dictionary_genres_lower for genre in chosen_genres_list):
                    filtered_movies.append(dictionary)

            else:  # Match any selected genre or single selected genre
                if any(genre in dictionary_genres_lower for genre in chosen_genres_list):
                    filtered_movies.append(dictionary)

    print(f"Genres filter applied. {len(filtered_movies)} movies remain.")

    return filtered_movies


# Spoken languages filter
def language_filter(movie_database, spoken_languages) -> Dict[str, str]:
    """
    The user chooses in which spoken languages they are interested and if all of them should be found in the movies.
    The functions checks if the input languages are properly spelled out (this is done by being found in a list of spoken languages).
    If there are multiple languages the function ofers a choice if all languages should be found in the movies or any language is okay.
    """

    chosen_spoken_language = input(str('Input chosen spoken language: '))
    language_filtering_option = ''
    if ',' in chosen_spoken_language:
        language_filtering_option = input(str('Would you like to: \na) Match all selected langauges \nb) Match any selected languages \nAnswer: ')).lower()
        
    spoken_language_check = chosen_spoken_language.lower()

    filtered_movies = []
    chosen_languages_list = [language.strip() for language in chosen_spoken_language.split(',')]

    for dictionary in movie_database:    
        if dictionary['spoken_languages']:        
            dictionary_spoken_language_lower = [language.strip().lower() for language in dictionary['spoken_languages'].split(",")]   
        
            if language_filtering_option == 'a':  # Match all selected langauges
                if all(language in dictionary_spoken_language_lower for language in chosen_languages_list):
                    filtered_movies.append(dictionary)

            else:  # Match any selected langauges or single selected langauge
                if any(language in dictionary_spoken_language_lower for language in chosen_languages_list):
                    filtered_movies.append(dictionary)
            
    print(f"Spoken Languages filter applied. {len(filtered_movies)} movies remain.")

    return filtered_movies


# Runtime filter
def runtime_filter(movie_database) -> Dict[str, str]:
    """
    The user chooses the runtime/s of the movies that they are intersted in.
    The user can choose either one or multiple runtime ranges.
    """

    print('Runtimes: \na) < 60 minutes \nb) 60 - 90 minutes \nc) 90 - 120 minutes \nd) 120 - 150 minutes \ne) > 150 minutes')
    chosen_runtime = input('Input chosen runtime (a, b, c, d, e): ').lower()

    inside_filtered_movies = []

    for dictionary in movie_database:    
        if dictionary['runtime']:
            runtime = int(dictionary['runtime'])
            for runtime_option in chosen_runtime.split(','):            
                if runtime_option.lower().strip() == "a" and runtime < 60:
                    inside_filtered_movies.append(dictionary)
                elif runtime_option.lower().strip() == "b" and 60 <= runtime <= 90:
                    inside_filtered_movies.append(dictionary)       
                elif runtime_option.lower().strip() == "c" and 90 < runtime <= 120:
                    inside_filtered_movies.append(dictionary)
                elif runtime_option.lower().strip() == "d" and 120 < runtime <= 150:
                    inside_filtered_movies.append(dictionary)
                elif runtime_option.lower().strip() == "e" and runtime > 150:
                    inside_filtered_movies.append(dictionary)

    filtered_movies = inside_filtered_movies
    print(f"Runtime filter applied. {len(filtered_movies)} movies remain.")

    return filtered_movies


# Score (vote_average) filter
def score_filter(movie_database) -> Dict[str, str]:
    """
    The user chooses the vote average/s of the movies that they are intersted in.
    The user can choose either one or multiple score ranges.
    """

    print('Scores: \na) > 1 \nb) 1 - 2 \nc) 2 - 3 \nd) 3 - 4 \ne) 4 - 5 \nf) 5 - 6 \ng) 6 - 7 \nh) 7 - 8 \ni) 8 - 9 \nj) 9 - 10 \nk) = 10')
    chosen_score = input('Input chosen score (a, b, c, d, e, f, g, h, i, j): ').lower()

    filtered_movies = []

    for dictionary in movie_database:    
        if dictionary['vote_average']:
            score = float(dictionary['vote_average'])
            for score_option in chosen_score.split(','):
                if score_option.strip() == "a" and score > 1:
                    filtered_movies.append(dictionary)
                elif score_option.strip() == "b" and 1 <= score <= 2:
                    filtered_movies.append(dictionary)
                elif score_option.strip() == "c" and 2 < score <= 3:
                    filtered_movies.append(dictionary)
                elif score_option.strip() == "d" and 3 < score <= 4:
                    filtered_movies.append(dictionary)
                elif score_option.strip() == "e" and 4 < score <= 5:
                    filtered_movies.append(dictionary)
                elif score_option.strip() == "f" and 5 < score <= 6:
                    filtered_movies.append(dictionary)
                elif score_option.strip() == "g" and 6 < score <= 7:
                    filtered_movies.append(dictionary)            
                elif score_option.strip() == "h" and 7 < score <= 8:
                    filtered_movies.append(dictionary)
                elif score_option.strip() == "i" and 8 < score <= 9:
                    filtered_movies.append(dictionary)
                elif score_option.strip() == "j" and 9 < score <= 10:
                    filtered_movies.append(dictionary)
                elif score_option == "k" and score == 10:
                    filtered_movies.append(dictionary)

    print(f"Score filter applied. {len(filtered_movies)} movies remain.")
    return filtered_movies


# Release date filter
def release_date_filter(movie_database) -> Dict[str, str]:
    """
    The user chooses the release date (year) or time period of the movies that they are intersted in.
    The user either chooses a certain year or a range inbetween years (both start and end year are included).
    The values in the year column are converted to datetime type before the check for validity of the movie year is done (if the year is in the range).
    """
    preliminary_release_date = input(str('Input chosen release year or years period (e.g. 2012-2015): '))    

    preliminary_release_date_v1 = preliminary_release_date.replace(" ", "")
    chosen_single_date_updated = ""
    first_range_date = ""
    second_range_date = ""

    filtered_movies = []

    if len(preliminary_release_date_v1) == 4:
        chosen_single_date_updated = datetime.strptime(preliminary_release_date_v1 + "-01-01", "%Y-%m-%d")        
        for dictionary in movie_database:    
            if dictionary['release_date']: 
                release_date = dictionary['release_date']
                if chosen_single_date_updated.year == dictionary['release_date'].year:
                    filtered_movies.append(dictionary)
    elif len(preliminary_release_date_v1) == 9 and preliminary_release_date_v1[4] == "-":
        first_range_date = datetime.strptime(preliminary_release_date_v1[:4] + "-01-01", "%Y-%m-%d")
        second_range_date = datetime.strptime(preliminary_release_date_v1[5:] + "-12-31", "%Y-%m-%d")
        for dictionary in movie_database:    
            if dictionary['release_date']:
                release_date = dictionary['release_date']
                if first_range_date.year <= release_date.year <= second_range_date.year:
                    filtered_movies.append(dictionary)    

    print(f"Release date filter applied. {len(filtered_movies)} movies remain.")
    return filtered_movies