# Movie-Trailer-Project 

A simple movie trailer website project for Udacity's full-stack [nanodegree program](https://www.udacity.com/nanodegree). The project demonstrates the use of a Movie object class in Python to generate a static webpage, which displays a listing of favorite movies and links each movie to its trailers video on YouTube. The project also includes some CSS and jQuery involved in the display of the webpage.  

## Demo

For a demo, check out <https://github.com/YVC07/Movie_trailer/blob/master/fresh_tomatoes.html>!

## Download

The files for the project, may be [downloaded here](https://github.com/YVC07/Movie_trailer).

### What's included

Within the download you'll find the following directories and files:

```
udacity-movie-trailer-project-master.zip/
├── css/
│   └── main.css
├── img/
│   └── curtains.jpg
├── js/
│   └── main.js
├── entertainment_center.py
├── fresh_tomatoes.html
├── fresh_tomatoes.py
├── media.py
└── README.md
```

## Documentation

### Movie object class

The Movie object class consists of four class variables, a simple constructor method, and a class method for playing a Movie object's movie trailer. The code is located in [media.py](https://github.com/YVC07/Movie_trailer/blob/master/media.py). 

##### constructor method

The constructor method is called when a new Movie object is created and must include four arguments -- [title](#movietitle), [year](#movieyear), [poster_url](#movieposter_url), and [trailer_url](#movietrailer_url). Each of these arguments is discussed further below.


###### movie.title

movie.title is any string used to identify the movie object.

###### movie.year

movie.year is an integer representing the year the movie was released.  

###### movie.poster_url

movie.poster_url is a string containing a URL linking to an image which will be used to represent the Movie object, such as a movie poster or DVD box cover. The movie trailer page portion of this project displays these images with a width of 188px and a height of 292px. So, images with a ratio of 1:1.5 will work best. 

###### movie.trailer_url

movie.trailer_url is a string containing a URL linking to the movie trailer on YouTube.com. The movie trailer page portion of the this project extracts the YouTube id from the URL, so while links to other video services are valid in the Movie class object, they will not work with the movie trailers page. 

##### show_trailer method

show_trailer can be called on any Movie class object to launch that object's movie trailer in a webpage. This method is useful for testing but is not used by the script that generates the finished movie trailers page.

### Movie Trailer Page Functions 

The functions used to create the final movie trailers page are located in [fresh_tomatoes.py](https://github.com/YVC07/Movie_trailer/blob/master/fresh_tomatoes.py), along with HTML template variables used by these functions. This file must be imported to access the functions described below.

#### open_movies_page function

To create the static movie trailers page the open_movies_page function must be called and supplied with one required argument (an array of Movie class objects) and one optional argument (a string specifying a sort order). If no sort order is specified or an unrecognized sort option is provided, the order the movies appear in the array will be used. Valid strings for specifying a sort order are:



The newly generated page will be placed in the same directory and named fresh_tomatoes.html. This new page relies on three files for its background image (img/curtains.jpg), CSS style settings (css/main.css), and jQuery effects (js/main.js).

#### create_movie_tiles_content

The create_movie_tiles_content function is called by the open_movies_page function. It takes the array of Movie class objects as an argument and iterates through each Movie object and applies the object's data to the portion of the HTML template for each movie. While iterating through each object's class variables, it extracts the YouTube id from movie.trailer_url.

#### sort_movie_data

The sort_movie_data function is called by the open_movies_page function. It takes two arguments the array of Movie class objects and the sort_option specify when open_movies_page was called (or "none" if no sort_option was provided). The function sorts the array, if needed and returns the array. 
