from typing import List, Dict, Set, Union
from datetime import datetime
from utils.libraries import open_movie_database

def correct_value_type(movie_database) -> Dict[str, Union[str, int, float]]:
    """
    Changes the type of some values to the correct type from a string for the equations for the normalized values that have to be done.
    """
    print("Editing value types...")
    for movie in movie_database:
        """
        The loop changes the value types of some fileds so that later in the program they don't need to be changed for every single use repetiotion
        """
        try:
            movie["vote_average"] = float(movie["vote_average"])
            movie["vote_count"] = int(movie["vote_count"])
            movie["revenue"] = float(movie["revenue"])
            movie["popularity"] = float(movie["popularity"])
            movie["release_date"] = datetime.strptime(movie['release_date'], "%Y-%m-%d")
        except:
            pass


    print("Value type edits done")
    return movie_database