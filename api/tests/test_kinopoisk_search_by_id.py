import allure
from api.clients.kinopoisk_client import KinopoiskClient
from config.settings import Settings


@allure.feature("API Тесты")
@allure.story("Поиск фильма по ID")
def test_search_movie_by_id():
    client = KinopoiskClient(base_url=Settings.KINOPOISK_API_URL, api_key=Settings.API_KEY)

    with allure.step("Ищем фильм по ID"):
        response = client.search_movie_by_id(258687)

    with allure.step("Проверяем результаты поиска"):
        assert response["name"] == "Интерстеллар"
