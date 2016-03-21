import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print(avatar.storyline)

#avatar.show_trailer()

star_wars = media.Movie("Star Wars", "An epic story set in a galaxy", "http://t0.gstatic.com/images?q=tbn:ANd9GcQZKZtrlY3dnzsjBIGKR_b1QhkgZfM4-FIcH61uHnLQRR3WpNhk", "https://www.youtube.com/watch?v=sGbxmsDFVnE")
#print(star_wars.storyline)

#star_wars.show_trailer()

movies = [toy_story, avatar, star_wars]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)

