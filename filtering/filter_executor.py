from typing import List, Dict, Set, Union
from filtering.filters import genre_filter, language_filter, runtime_filter, score_filter, release_date_filter
from filtering.filter_selector import filter_selection
from utils.data_value_type_editor import correct_value_type


def filter_movies(movie_database, filters_to_apply, movie_genres, spoken_languages) -> Dict[str, str]:
    """
    The filters that the user has chosen are applied and a list of filtered movies is returned.
    Using a dictionary of the filter functions with numbers for keys. 
    Then iterate over the list of chosen filters and check if the iteration can be found in the keys.
    We use a copy of the database in order to avoid manipulating the data inside the original as later we manipulate the data type of some field values
    """

    pre_filtered_movies = movie_database.copy()

    filters = {"1": (genre_filter, movie_genres), "2": (language_filter, spoken_languages), "3": (runtime_filter,), "4": (score_filter,), "5": (release_date_filter,)}
    """
    filters is a dictionary with tuples in order to use *args later in the function in order to use different functions with different arguments
    """


    for filter_choice in filters_to_apply:
        if filter_choice in filters:
            filter_function, *args = filters[filter_choice] # Unpack the value of the chosen filter
            pre_filtered_movies = filter_function(pre_filtered_movies, *args) # Based on the number that is iterated, this pulls the said filter function 
                                                                              # for execution and gives as an argument a copy of the movie database and 
                                                                              # an additional argument if needed

    filtered_movies = pre_filtered_movies
    return filtered_movies