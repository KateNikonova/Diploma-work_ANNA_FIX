import allure
import pytest
from ui.pages.kinopoisk_search_page import KinopoiskSearchPage


@allure.feature("Поиск фильма")
@allure.story("Поиск с пустым полем")
def test_empty_search(driver):
    search_page = KinopoiskSearchPage(driver)
    search_page.search_movie_by_title("")

    with allure.step("Проверить сообщение об ошибке"):
        assert "Введите название фильма" in driver.page_source