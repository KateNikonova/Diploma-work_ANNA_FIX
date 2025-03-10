import allure
import pytest
from api.clients.kinopoisk_client import KinopoiskClient
from config.settings import Settings


@allure.feature("API Тесты")
@allure.story("Поиск фильма по жанру")
@pytest.mark.parametrize("genre", ["фантастика",
                                  "комедия",
                                  "ужасы",
                                  "мелодрама",
                                  "для взрослых",
                                  "ток-шоу"])
def test_search_movie_by_genre(genre):
    client = KinopoiskClient(base_url=Settings.KINOPOISK_API_URL, api_key=Settings.API_KEY)

    with allure.step("Ищем фильм по жанру"):
        response = client.search_movie_by_genre(genre)

    with allure.step("Проверяем результаты поиска"):
        assert len(response["docs"]) > 0
