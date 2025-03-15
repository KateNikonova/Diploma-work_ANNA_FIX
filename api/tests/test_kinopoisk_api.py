import allure
import pytest
from api.clients.kinopoisk_client import KinopoiskClient
from api.schemas.kinopoisk_schemas import movie_schema


@allure.feature("API Тесты")
@allure.story("Поиск фильма на Кинопоиске")
def test_search_movie():
    client = KinopoiskClient(base_url="https://api.kinopoisk.dev")

    with allure.step("Ищем фильм по названию"):
        response = client.search_movie(title="Интерстеллар")

    with allure.step("Проверяем ответ API"):
        assert response["title"] == "Интерстеллар"
        assert response["year"] == 2014




















#авторизация
#поиск фильма по названию
#поиск фильма по жанру
#оценить фильм
#поиск с пустым полем
#добавить фильм в закладки