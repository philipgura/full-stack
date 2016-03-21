import media
import fresh_tomatoes

#make a movie list
movies = []
movies.append(media.Movie("Indiana Jones and the Raiders of the Lost Ark", "https://studycentersonline.org/wp-content/uploads/2015/04/Raiders.jpg", "https://www.youtube.com/watch?v=gz4crpFaW4M", "1981", "PG"))
movies.append(media.Movie("Avatar", "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp", "https://www.youtube.com/watch?v=cRdxXPV9GNQ", "2009", "PG-13"))
movies.append(media.Movie("Star Wars: The Force Awakens", "http://t0.gstatic.com/images?q=tbn:ANd9GcQZKZtrlY3dnzsjBIGKR_b1QhkgZfM4-FIcH61uHnLQRR3WpNhk", "https://www.youtube.com/watch?v=sGbxmsDFVnE", "2015", "PG-13"))
movies.append(media.Movie("Blade Runner", "http://t3.gstatic.com/images?q=tbn:ANd9GcTcvek3p12Gwqwk-2wjTSHWTNq0LTTeoOgXUwqerVOY2u9zjOgO", "https://www.youtube.com/watch?v=3qZSIla_zPQ", "1982", "R"))
movies.append(media.Movie("The Fountain", "http://www.gstatic.com/tv/thumb/dvdboxart/159471/p159471_d_v8_aa.jpg", "https://www.youtube.com/watch?v=u47Dl_I8ums", "2006", "PG-13"))
movies.append(media.Movie("Zoolander", "http://www.gstatic.com/tv/thumb/movieposters/28447/p28447_p_v8_ac.jpg", "https://www.youtube.com/watch?v=YtQq0T3ExLs", "2001", "PG-13"))

#build html page
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)

