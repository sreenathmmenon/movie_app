import fresh_tomatoes
import movie_api

class Movie():
    """
    Movie Class gets the movie name, pass the details to OMDB API and
    fetch all the details related to that movie (if available)

    Attributes:
        name (str): name of the movie
        trailer (str): youtube link for the movie trailer
    """
    def __init__(self, name, trailer):
        """Constructor method"""

        #Pass the movie name to OMDB API
        movie = movie_api.MovieApi(name)

        #Fetch the details related to the movie
        self.title = movie.get_title()
        self.director = movie.get_director()
        self.production = movie.get_production()
        self.poster_image_url = movie.get_poster_url()
        self.genre = movie.get_genre()
        self.released = movie.get_release_date()
        self.imdb_rating = movie.get_rating()
        self.trailer_youtube_url = trailer
