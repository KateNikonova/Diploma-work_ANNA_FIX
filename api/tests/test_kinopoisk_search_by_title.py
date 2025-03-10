import allure
import pytest
from api.clients.kinopoisk_client import KinopoiskClient
from config.settings import Settings

@allure.feature("API Тесты")
@allure.story("Поиск фильма по названию")
def test_search_movie_by_title():
    client = KinopoiskClient(base_url=Settings.KINOPOISK_API_URL, api_key=Settings.API_KEY)

    with allure.step("Ищем фильм по названию"):
        response = client.search_movie_by_title("Интерстеллар")

    with allure.step("Проверяем результаты поиска"):
        assert response["docs"][0]["name"] == "Интерстеллар"