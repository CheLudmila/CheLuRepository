from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    # кнопка "Sign up"
    SIGN_UP_BTN = (By.XPATH, "//button[contains(text(),'Sign up')]")
