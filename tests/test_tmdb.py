import pytest
import tmdb_client
from unittest.mock import Mock
import requests
from main import app

def test_get_poster_url_uses_default_size():
   # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url

def test_get_single_movie(monkeypatch):
   mock_single_movie = 000000
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   single_movie = tmdb_client.get_single_movie(movie_id=602211)
   assert single_movie == mock_single_movie

def test_get_movie_images_backdrops(monkeypatch):
   mock_movie_images_backdrops = {}
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie_images_backdrops
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   mock_movie_images = tmdb_client.get_movie_images_backdrops(movie_id=000000)
   assert mock_movie_images == mock_movie_images_backdrops

def test_get_single_movie_cast(monkeypatch):
   mock_single_movie_cast = {}
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   mock_movie_cast = tmdb_client.get_single_movie_cast(movie_id=000000)
   assert mock_movie_cast == mock_single_movie_cast

def test_get_movies_list(monkeypatch):
   list_type = ["popular", "upcoming", "top rated", "now playing"]
   for i in list_type:
      mock_movies_list = ['Movie 1', 'Movie 2']
      requests_mock = Mock()
      response = requests_mock.return_value
      response.json.return_value = mock_movies_list
      monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

      movies_list = tmdb_client.get_movies_list(list_type=i)
      assert movies_list == mock_movies_list

@pytest.mark.parametrize('list_type, result', (
   ("popular", 200),
   ("upcoming", 200),
   ("top_rated", 200),
   ("now_playing", 200),
))
def test_homepage(monkeypatch, list_type, result):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get(f'/?list_type={list_type}')
       assert response.status_code == result
       api_mock.assert_called_once_with(f'movie/{list_type}')

# def test_homepage(monkeypatch):
#    api_mock = Mock(return_value={'results': []})
#    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

#    with app.test_client() as client:
#        response = client.get('/')
#        assert response.status_code == 200
#        api_mock.assert_called_once_with('movie/popular')

# def test_get_movies_list_top_rated(monkeypatch):
#    mock_movies_list = ['Movie 1', 'Movie 2']
#    requests_mock = Mock()
#    response = requests_mock.return_value
#    response.json.return_value = mock_movies_list
#    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

#    movies_list = tmdb_client.get_movies_list(list_type="top rated")
#    assert movies_list == mock_movies_list

# def test_get_movies_list_upcoming(monkeypatch):
#    mock_movies_list = ['Movie 1', 'Movie 2']
#    requests_mock = Mock()
#    response = requests_mock.return_value
#    response.json.return_value = mock_movies_list
#    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

#    movies_list = tmdb_client.get_movies_list(list_type="upcoming")
#    assert movies_list == mock_movies_list

# def test_get_movies_list_now_playing(monkeypatch):
#    mock_movies_list = ['Movie 1', 'Movie 2']
#    requests_mock = Mock()
#    response = requests_mock.return_value
#    response.json.return_value = mock_movies_list
#    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

#    movies_list = tmdb_client.get_movies_list(list_type="now playing")
#    assert movies_list == mock_movies_list

# def test_get_movies_list_type_popular():
#    movies_list = tmdb_client.get_movies_list(list_type="popular")
#    assert movies_list is not None

# def test_get_movies_list(monkeypatch):
#    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
#    mock_movies_list = ['Movie 1', 'Movie 2']

#    requests_mock = Mock()
#    # Wynik wywołania zapytania do API
#    response = requests_mock.return_value
#    # Przysłaniamy wynik wywołania metody .json()
#    response.json.return_value = mock_movies_list
#    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

#    movies_list = tmdb_client.get_movies_list(list_type="popular")
#    assert movies_list == mock_movies_list

