from typing import List, Dict, Set, Union
from datetime import datetime

# Class for a Temporary User
class temp_user:
    """
    This calls creates a temporary user that afterwards gets to make choices about filters, movies, etc.
    """

    def __init__(self, name): # Initialize the instance of the user and variables
        self.name = name
        self.liked_movies = set()  # Variable to collect the movies the user liked - using set() in order to avoid having duplicates
        self.disliked_movies = set()  # Variable to collect the movies the user disliked - using set() in order to avoid having duplicates

    def like_movie(self, movie): # Add a movie to the user's liked list
        self.liked_movies.add(movie)

    def dislike_movie(self, movie): # Add a movie to the user's disliked list
        self.disliked_movies.add(movie)

    def get_preferences(self) -> Dict[str, Set[Dict[str, Union[str, int, float, datetime]]]]: # Return the user's liked and disliked movies
        return {"liked": self.liked_movies, 
                "disliked": self.disliked_movies,
        }