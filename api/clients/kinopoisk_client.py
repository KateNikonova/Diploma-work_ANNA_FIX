import requests


class KinopoiskClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {"X-API-KEY": api_key}

    def search_movie_by_title(self, title):
        response = requests.get(f"{self.base_url}/v1.4/movie/search", params={"query": title}, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def search_movie_by_genre(self, genre):
        response = requests.get(f"{self.base_url}/v1.4/movie", params={"genres.name": genre}, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def search_movie_by_year(self, year):
        response = requests.get(f"{self.base_url}/v1.4/movie", params={"year": year}, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def search_movie_by_id(self, movie_id):
        response = requests.get(f"{self.base_url}/v1.4/movie/{movie_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def search_movie_empty_query(self):
        response = requests.get(f"{self.base_url}/v1.4/movie/search", params={"query": ""}, headers=self.headers)
        return response

    def search_movie_invalid_method(self):
        response = requests.post(f"{self.base_url}/v1.4/movie/search", headers=self.headers)
        return response
