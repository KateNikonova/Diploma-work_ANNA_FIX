import allure
import pytest
from api.clients.kinopoisk_client import KinopoiskClient
from config.settings import Settings


@allure.feature("API Тесты")
@allure.story("Поиск фильма по году выпуска")
def test_search_movie_by_year():
    client = KinopoiskClient(base_url=Settings.KINOPOISK_API_URL, api_key=Settings.API_KEY)

    with allure.step("Ищем фильм по году выпуска"):
        response = client.search_movie_by_year(2014)

    with allure.step("Проверяем результаты поиска"):
        assert response["docs"][0]["year"] == 2014