import allure
import pytest
from ui.pages.kinopoisk_search_page import KinopoiskSearchPage
from config.settings import Settings


@allure.feature("Поиск фильма")
@allure.story("Поиск фильма по названию")
def test_search_movie_by_title(driver):
    search_page = KinopoiskSearchPage(driver)
    search_page.search_movie_by_title("Интерстеллар")

    with allure.step("Проверить результаты поиска"):
        assert "Интерстеллар" in search_page.get_first_movie_title()


@allure.feature("Поиск фильма")
@allure.story("Поиск фильма по жанру")
def test_search_movie_by_genre(driver):
    search_page = KinopoiskSearchPage(driver)
    search_page.search_movie_by_genre("Фантастика")

    with allure.step("Проверить результаты поиска"):
        assert search_page.get_search_results()