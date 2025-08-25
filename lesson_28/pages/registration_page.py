from selenium.webdriver.common.by import By
from .base_page import BasePage


from selenium.webdriver.common.by import By
from .base_page import BasePage


class RegistrationPage(BasePage):
    # поля форми
    NAME_INPUT = (By.ID, "signupName")
    LASTNAME_INPUT = (By.ID, "signupLastName")
    EMAIL_INPUT = (By.ID, "signupEmail")
    PASSWORD_INPUT = (By.ID, "signupPassword")
    REPASSWORD_INPUT = (By.ID, "signupRepeatPassword")

    # кнопка "Register"
    REGISTER_BTN = (By.XPATH, "//button[contains(text(),'Register')]")

    # заголовок сторінки Garage
    GARAGE_TITLE = (By.XPATH, "//h1[text()='Garage']")