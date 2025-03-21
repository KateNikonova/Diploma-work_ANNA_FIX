from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage


class KinopoiskLoginPage(BasePage):
    LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), 'Войти')]")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Мой профиль')]")
    USER_AVATAR = (By.XPATH, "//div[@class='user-avatar']")  # Пример локатора для аватара пользователя
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get("https://www.kinopoisk.ru/")
        self.click(self.LOGIN_BUTTON)

    def enter_email(self, email):
        self.send_keys(self.EMAIL_FIELD, email)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    def submit_login_form(self):
        self.click(self.SUBMIT_BUTTON)

    def is_profile_link_visible(self):
        return self.is_visible(self.PROFILE_LINK)

    def is_logged_in(self):
        """Проверка, что пользователь авторизован."""
        try:
            self.wait.until(EC.presence_of_element_located(self.USER_AVATAR))
            return True
        except:
            return False