import allure
import pytest
from api.clients.kinopoisk_client import KinopoiskClient
from config.settings import Settings


@allure.feature("API Тесты")
@allure.story("Поиск с пустым запросом")
@pytest.mark.xfail # есть баг пока отмечен xfail
def test_search_movie_empty_query():
    client = KinopoiskClient(base_url=Settings.KINOPOISK_API_URL, api_key=Settings.API_KEY)

    with allure.step("Ищем фильм с пустым запросом"):
        response = client.search_movie_empty_query()

    with allure.step("Проверяем статус код"):
        assert response.status_code == 400
