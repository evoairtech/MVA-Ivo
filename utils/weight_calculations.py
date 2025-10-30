from typing import List, Dict, Set, Union
from filtering.filter_executor import filter_movies



def value_normalize(value, min_value, max_value) -> float:
    """
    We'll use normalized values for the vote_count, vote_average, revenue and popularity factors in order to get an indicator of the quality/likeability of a movie.
    value = value of the used property, value_min = the min value found for that factor in the filtered list, value_max = the max value found for that factor in the filtered list.
    """
    return (value - min_value) / (max_value - min_value) if max_value > min_value else 0


def min_max_value(filtered_movies) -> Dict[str, Union[int, float]]:
    """
    Finding the min and max values of the used factors in order to calculate the normalized values of movies.
    Returning a dictionary makes it easier to access the values later on.
    """

    return {
        "min_vote_average" : min(movie["vote_average"] for movie in filtered_movies),
        "max_vote_average" : max(movie["vote_average"] for movie in filtered_movies),
        "min_vote_count" : min(movie["vote_count"] for movie in filtered_movies),
        "max_vote_count" : max(movie["vote_count"] for movie in filtered_movies),
        "min_revenue" : min(movie["revenue"] for movie in filtered_movies),
        "max_revenue" : max(movie["revenue"] for movie in filtered_movies),
        "min_popularity" : min(movie["popularity"] for movie in filtered_movies),
        "max_popularity" : max(movie["popularity"] for movie in filtered_movies)
    }


# Weights for each factor
def factor_weight() -> Dict[str, float]:
    """
    Weight of factors that will be used (could be turned into an input to let users choose their own factor weights).
    """

    return {
    "W_va" : 0.3,  # Weight for vote_average 
    "W_vc" : 0.25,  # Weight for vote_count 
    "W_r" : 0.35, # Weight for revenue 
    "W_p" : 0.1,  # Weight for popularity
    }


# Calculate the movie Score Weight
def calc_movie_score_weight(filtered_movies, min_max_value, factor_weight) -> Dict[str, Union[str, int, float]]:
    """
    The function calculates the nozmalized values for every factor using the using the value_normalize function,
    and then it calculates the overall movie weight using the normalized factor values and the factor weights.
    The function calls the values returned as dictionary in both min_max_value and factor_weight functions.
    """

    for movie in filtered_movies:
        normalized_vote_average = value_normalize(movie["vote_average"], min_max_value["min_vote_average"], min_max_value["max_vote_average"])
        normalized_vote_count = value_normalize(movie["vote_count"], min_max_value["min_vote_count"], min_max_value["max_vote_count"])
        normalized_revenue = value_normalize(movie["revenue"], min_max_value["min_revenue"], min_max_value["max_revenue"])
        normalized_popularity = value_normalize(movie["popularity"], min_max_value["min_popularity"], min_max_value["max_popularity"])
    
        movie["score_weight"] = (factor_weight["W_va"] * normalized_vote_average + factor_weight["W_vc"] * normalized_vote_count + factor_weight["W_r"] * normalized_revenue + factor_weight["W_p"] * normalized_popularity)

    return filtered_movies