import webbrowser


class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, poster_image, trailer, year, rating):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
        self.release_year = year
        self.setRating(rating)

    def setRating(self, rating):
        if(rating in self.VALID_RATINGS):
            self.rating = rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
