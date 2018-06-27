import requests as req


class MovieApi():
    """
    Wrapper to connect to OMDB API and fetch the movie details

    Attributes:
        movie_name: name of the movie whose details are to be obtained
    """

    # Defining constants for API key (account specific) and OMDB API url
    API_KEY = 'b6d9a50d'
    OMDB_API_URL = 'http://www.omdbapi.com/?t='

    def __init__(self, movie_name):
        """Constructor method"""
        # Fetch the move name and replace space(if present) with + symbol
        self.movie_name = movie_name
        movie_name.replace(" ", "+")

        # Pass the movie name to OMDB API and fetch the json response
        response = req.get(self.OMDB_API_URL + movie_name +
                           '&apikey=' + self.API_KEY)
        self.data = response.json()

    def get_title(self):
        """
        Fetch Title from Output

        Args
            N/A

        Returns:
            Returns movie title if available. Else, return None
        """
        return self.data.get('Title')

    def get_director(self):
        """
        Fetch the Director Name from the Output

        Args
            N/A

        Returns:
            Returns director name if available. Else, return None
        """
        return self.data.get('Director')

    def get_production(self):
        """
        Fetch the Production Name from the Output

        Args
            N/A

        Returns:
            Returns production name if available. Else, return None
        """
        return self.data.get('Production')

    def get_poster_url(self):
        """
        Fetch the Url to the poster image

        Args
            N/A

        Returns:
            Returns movie's poster url if available. Else, return None
        """
        return self.data.get('Poster')

    def get_genre(self):
        """
        Fetch the movie genre data

        Args
            N/A

        Returns:
            Returns movie genre data if available. Else, return None
        """
        return self.data.get('Genre')

    def get_release_date(self):
        """
        Fetch the Movie Release Data

        Args
            N/A

        Returns:
            Returns movie release data if available. Else, return None
        """
        return self.data.get('Released')

    def get_rating(self):
        """
        Fetch the Movie's IMDB Rating

        Args
            N/A

        Returns:
            Returns movie's IMDB rating if available. Else, return None
        """
        return self.data.get('imdbRating')
