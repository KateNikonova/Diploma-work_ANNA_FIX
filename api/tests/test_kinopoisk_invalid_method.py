import allure
import pytest
from api.clients.kinopoisk_client import KinopoiskClient
from config.settings import Settings

@allure.feature("API Тесты")
@allure.story("Поиск с неправильным методом")
def test_search_movie_invalid_method():
    client = KinopoiskClient(base_url=Settings.KINOPOISK_API_URL, api_key=Settings.API_KEY)

    with allure.step("Используем неправильный метод для поиска"):
        response = client.search_movie_invalid_method()

    with allure.step("Проверяем статус код"):
        assert response.status_code == 405