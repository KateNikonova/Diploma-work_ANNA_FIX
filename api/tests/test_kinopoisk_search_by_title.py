import allure
import pytest
from api.clients.kinopoisk_client import KinopoiskClient
from config.settings import Settings


@allure.feature("API Тесты")
@allure.story("Поиск фильма по названию")
@pytest.mark.parametrize("title", ["Дюна",
                                  "Титаник",
                                  "1+1",
                                  "Анора",
                                  "Три кота",
                                  "Я, снова я и Ирэн"])
def test_search_movie_by_title(title):
    client = KinopoiskClient(base_url=Settings.KINOPOISK_API_URL, api_key=Settings.API_KEY)

    with allure.step("Ищем фильм по названию"):
        response = client.search_movie_by_title(title)

    with allure.step("Проверяем результаты поиска"):
        assert response["docs"][0]["name"] == title
