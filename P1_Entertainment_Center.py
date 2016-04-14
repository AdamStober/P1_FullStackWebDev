# Import Libraries to access Movies class and Web Browser Structure

import P1_fresh_tomatoes
import P1_media

# Create Movies instances.  Parameters are:
## Title
## Tagline
## Movie Poster (URL of jpg)
## Movie Trailer (YouTube URL)

toy_story = P1_media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
the_mask = P1_media.Movie("The Mask",
                       "From Zero to Hero",
                       "http://ia.media-imdb.com/images/M/MV5BMTg0Mjc1NzQzNF5BMl5BanBnXkFtZTcwODY3MDEzMQ@@._V1_SX640_SY720_.jpg",
                       "https://www.youtube.com/watch?v=hOqVRwGVUkA")
gladiator = P1_media.Movie("Gladiator",
                        "A Hero Will Rise",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=AxQajgTyLcM")

# Create List of Movies
movies = [toy_story, the_mask, gladiator]

# Display movies in browser
P1_fresh_tomatoes.open_movies_page(movies)
