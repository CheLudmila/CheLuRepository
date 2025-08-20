from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class NovaPoshtaTracker:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_page(self):
        self.driver.get("https://tracking.novaposhta.ua/#/uk")

    def get_status_by_number(self, tracking_number: str) -> str:
        # Чекаємо появи поля введення
        input_field = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[type='text']")
        ))
        input_field.clear()
        input_field.send_keys(tracking_number)
        input_field.send_keys(Keys.ENTER)

        # Чекаємо появи статусу
        try:
            status_div = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.header__status-text")
            ))
            return status_div.text.strip()
        except:
            return "Статус не знайдено або накладна відсутня"


@pytest.mark.parametrize("tracking_number, expected_status", [
    ("20710222208064", "Отримана"),  # приклад дійсного номера
    ("0000000000", "Статус не знайдено або накладна відсутня"),  # приклад невірного номера
])
def test_tracking_status(tracking_number, expected_status):
    driver = webdriver.Chrome()
    driver.maximize_window()

    tracker = NovaPoshtaTracker(driver)
    tracker.open_page()
    status = tracker.get_status_by_number(tracking_number)
    driver.quit()

    assert status == expected_status