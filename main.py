from flask import Flask, render_template
import tmdb_client
import random
from flask import request
from flask import abort
import requests


app = Flask(__name__)

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    try:
        movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    except:
        movies = tmdb_client.get_movies(how_many=8, list_type="popular")
    selected_movie = selected_list
    movie_lists = ["now_playing", "popular", "top_rated", "upcoming"]
    return render_template("homepage.html", movies=movies, movie_lists=movie_lists, selected_movie=selected_movie)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_cast(movie_id, how_many=4)
    backdrops = tmdb_client.get_movie_images_backdrops(movie_id)['backdrops']
    backdrops = random.choice(backdrops)
    return render_template("movie_details.html", movie=details, cast=cast, backdrops=backdrops)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

if __name__ == '__main__':
    app.run(debug=True)
