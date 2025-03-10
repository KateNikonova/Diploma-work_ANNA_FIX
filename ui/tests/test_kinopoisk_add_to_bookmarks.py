import allure
import pytest
from ui.pages.kinopoisk_movie_page import KinopoiskMoviePage
from ui.pages.kinopoisk_profile_page import KinopoiskProfilePage


@allure.feature("Закладки")
@allure.story("Добавление фильма в закладки")
def test_add_to_bookmarks(driver):
    movie_page = KinopoiskMoviePage(driver)
    movie_page.add_to_bookmarks()

    with allure.step("Проверить успешность добавления"):
        assert movie_page.is_success_message_visible()

    profile_page = KinopoiskProfilePage(driver)
    profile_page.open_bookmarks()

    with allure.step("Проверить наличие фильма в закладках"):
        assert len(profile_page.get_bookmarked_movies()) > 0