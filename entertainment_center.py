import media
import fresh_tomatoes

voz = media.Movie("Vunnadi Okkate Zindagi", "Friendship",
                  "http://data1.ibtimes.co.in/cache-img-0-450/en/"
                  "full/666658/1509075597_unnadi-okate-zindagi.jpg",
                  "https://www.youtube.com/watch?v=7iWnyBNmgSs")
# print(voz.storyline)
toystory = media.Movie("Toy Story", "Toy Story",
                       "https://upload.wikimedia.org/"
                       "wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")
toliprema = media.Movie("Toliprema", "Toliprema",
                        "http://www.ratingdada.com/images/"
                        "3/12212017010206pm_tholi-prema.jpg",
                        "https://www.youtube.com/watch?v=-kFvrsAgp3M")
bagamathi = media.Movie("Bagamathi", "Chanchala",
                        "http://www.bollywoodlife.com/wp-content/"
                        "uploads/2018/01/bhaagamathie-box-office-280118.jpg",
                        "https://www.youtube.com/watch?v=Aahj3atxdS4")
rangasthalam = media.Movie("Rangasthalam", "Movie",
                           "https://www.25cineframes.com/images/gallery/"
                           "2017/11/rangasthalam-movie-"
                           "hd-photos-stills-ram-charan-"
                           "samantha-akkineni-images-gallery/"
                           "61-Rangasthalam-Movie-"
                           "HD-Photos-Stills-Ram-Charan-Samantha-"
                           "Akkineni-Images-Gallery.jpg",
                           "https://www.youtube.com/watch?v=Nui2btXQj_c")
# voz.show_trailer()

movies = [voz, toystory, toliprema, bagamathi, rangasthalam]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.__doc__)
