from selenium.webdriver.common.by import By
from .base_page import BasePage

class KinopoiskSearchPage(BasePage):
    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(text(), 'Найти')]")
    SEARCH_RESULTS = (By.CLASS_NAME, "search-results")
    GENRE_FILTER = (By.XPATH, "//div[contains(text(), 'Жанр')]")
    MOVIE_TITLE = (By.CLASS_NAME, "movie-title")

    def __init__(self, driver):
        super().__init__(driver)

    def search_movie_by_title(self, title):
        self.send_keys(self.SEARCH_FIELD, title)
        self.click(self.SEARCH_BUTTON)

    def search_movie_by_genre(self, genre):
        self.click(self.GENRE_FILTER)
        self.click((By.XPATH, f"//div[contains(text(), '{genre}')]"))

    def get_search_results(self):
        return self.is_visible(self.SEARCH_RESULTS)

    def get_first_movie_title(self):
        return self.is_visible(self.MOVIE_TITLE).text