import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.kinopoisk_login_page import KinopoiskLoginPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.feature("UI Тесты")
@allure.story("Авторизация на Кинопоиске")
def test_kinopoisk_login(driver):
    login_page = KinopoiskLoginPage(driver)

    with allure.step("Открыть главную страницу Кинопоиска"):
        login_page.open_login_page()

    with allure.step("Ввести email"):
        login_page.enter_email("your_email@example.com")

    with allure.step("Ввести пароль"):
        login_page.enter_password("your_password")

    with allure.step("Отправить форму авторизации"):
        login_page.submit_login_form()

    with allure.step("Проверить успешность авторизации"):
        assert login_page.is_profile_link_visible(), "Авторизация не удалась!"

    allure.attach(driver.get_screenshot_as_png(), name="Скриншот после авторизации", attachment_type=allure.attachment_type.PNG)


























#авторизация
#поиск фильма по названию
#поиск фильма по жанру
#оценить фильм
#поиск с пустым полем
#добавить фильм в закладки
