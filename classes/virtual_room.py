from typing import List, Dict, Set, Union
from datetime import datetime

# Class for the Virtual room that will hold the users who are gathered together
class virtual_room:
    """
    This class creates a virtual room where users will enter in order to participate together in the movie selection process.
    Each user receives the same list of movies which has been selected based on previously defined filters (defined by a user).
    """
    def __init__(self, movie_list):
        self.users = []  # Variable for the list of users in the room
        self.movie_list = movie_list # Predifined list of movies created by the used filters

    def add_user(self, user): # Add a user to the virtual room
        self.users.append(user)

    def show_movies_to_user(self, user):  
        """
        This method does two thing (the logic should be further extended in the future):
        1) Checks if the movie shown to the user is the first movies shown to this user (used for the ordering logic),
        2) Keeps showing the user movies and the users keeps giving answers (intersted or not) until they decide to stop.
        """
        first_shown_movie = True   
        
        print(f'\nUser: {user.name}')

        # Shows the movies one-by-one to the user and he choses if he's interested or not
        for movie in self.movie_list:
            #print(f"{movie['title']}: {movie['score_weight']:.4f}")    
            if first_shown_movie: # Flag checks if the movie is the first one to be shown (if first_shown_movie == True)
                print(f"\nMovie: {movie['title']} | Release date: {movie['release_date']} | Runtime: {movie['runtime']} \nOverview: {movie['overview']}")
                answer = input("\nWould you like to watch this movie? Y = yes | N = No | E = End selection \nAnswer: ")
                if answer.lower() == "y":
                    user.like_movie(movie["title"])
                elif answer.lower() == "n":
                    user.dislike_movie(movie["title"])
                elif answer.lower() == "e":
                    break
                first_shown_movie = False # Set flag to False to prevent this block from running again
            else:
                 print(f"\nMovie: {movie['title']} | Release date: {movie['release_date']} | Runtime: {movie['runtime']} \nOverview: {movie['overview']}")
                 answer = input("\nWould you like to watch this movie? Y = yes | N = No | E = End selection \nAnswer: ")
                 if answer.lower() == "y":
                     user.like_movie(movie["title"])
                 elif answer.lower() == "n":
                     user.dislike_movie(movie["title"])
                 elif answer.lower() == "e":
                     break
               
    def analyze_preferences(self) -> Dict[str, Union[Set[str], Dict[str, Union[str, int, float, datetime]]]]:
        """
        The method analyzes the results of the provided choices from the users.
        Explanation of the logic:
        1) Creates a set of movies liked by one of the users based on their list or liked movies
        2) Then it checks the list of liked movies of the next users compared to that set and leaves in it only the matching in both the set and the list movies
        3) Using a set as sets don't let duplicates be created
        
        The other  thing that the method does is that it creates a set of all liked movies and uses it to find movies that are liked by most users (used as a back up
        if there aren't any movies that have been liked by all users).
        After that it checks in how many user lists they are found (provides a point for every match) and then creates a dictionary with the movie and the number of likes 
        that the movies has had (there are set conditions depending on the amount of users as to how many likes a movie must have 
        in order to appear in the liked_by_most dictionary).
        """

        liked_by_all = set(self.users[0].liked_movies) if self.users else set() # The set is modified by the code in the next rows
        liked_by_most = {}
        liked_movies = set()
        user_count = len(self.users)
        threshold = user_count * 0.8

        for user in self.users:
            liked_movies.update(user.liked_movies)  # Track all liked movies
            liked_by_all &= user.liked_movies  # Check what movies are in both lists and leave in "liked_by_all" only the the ones intersecting

        # Find movies liked by most for less than 5 users and at least 80% of the users with 6 and above
        for movie in liked_movies:
            count_likes = sum(1 for user in self.users if movie in user.liked_movies and movie not in liked_by_all)
            if user_count <= 5 and count_likes >= user_count - 1: # Liked by all but one user                 
                liked_by_most[movie] = count_likes # Add a Key:Value pair to the dictionary "liked_by_most" - movie:count_likes
            elif user_count > 5 and count_likes >= threshold: # Liked by at least 80% of the users               
                liked_by_most[movie] = count_likes

        return {
            "liked_by_all": liked_by_all,
            "liked_by_most": liked_by_most,
        }