from media import Movie
import fresh_tomatoes

# Dictionary mapping movie names with their youtube trailer url's
trailers = {'avatar': 'https://www.youtube.com/watch?v=5PSNL1qE6VY',
            'moana': 'https://www.youtube.com/watch?v=LKFuXETZUsI',
            'shrek': 'https://www.youtube.com/watch?v=W37DlG1i61s',
            'zootopia': 'https://www.youtube.com/watch?v=bY73vFGhSVk',
            'pinocchio': 'https://www.youtube.com/watch?v=jHI_0dlzqFo',
            'toystory3': 'https://www.youtube.com/watch?v=JcpWXaA2qeg',
            'incredibles': 'https://www.youtube.com/watch?v=eZbzbC9285I',
            'dragon': 'https://www.youtube.com/watch?v=oKiYuIsPxYk',
            'snow_white': 'https://www.youtube.com/watch?v=JtWcPgDjPrM'
           }

# Creating movie objects by passing movie name and trailer url to Movie class
avatar = Movie('avatar', trailers.get('avatar'))
moana  = Movie('moana', trailers.get('moana'))
shrek  = Movie('shrek', trailers.get('shrek'))
snow_white = Movie('snow white and the seven dwarfs', trailers.get('snow_white'))
zootopia = Movie('zootopia', trailers.get('zootopia'))
pinocchio = Movie('pinocchio', trailers.get('pinocchio'))
toystory3 = Movie('toy story 3', trailers.get('toystory3')) 
incredibles = Movie('the incredibles', trailers.get('incredibles'))
dragon = Movie('how to train your dragon', trailers.get('dragon'))

# Create a list of all movie objects
movies = [toystory3, dragon, zootopia, incredibles, shrek, avatar, snow_white, moana, pinocchio]

# Pass the movie objects and open the movie website
fresh_tomatoes.open_movies_page(movies)
