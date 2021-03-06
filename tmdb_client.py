import requests
import random
import pytest
import os
API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")


# def get_movies_list(list_type):
#     endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     response.raise_for_status()
#     return response.json()
# print(get_popular_movies())

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movie_images_backdrops(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)["results"]
    random.shuffle(data)
    return data[:how_many]

def get_cast(movie_id, how_many):
    data = get_single_movie_cast(movie_id)["cast"]
    return data[:how_many]

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_movies_list(list_type):
   return call_tmdb_api(f"movie/{list_type}")