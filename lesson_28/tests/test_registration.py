import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_user_registration(driver):
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign up')]"))
    ).click()

    email = f"testuser_{int(time.time())}@example.com"
    password = "Qwerty123!"

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "signupName"))
    ).send_keys("Test")

    driver.find_element(By.ID, "signupLastName").send_keys("User")
    driver.find_element(By.ID, "signupEmail").send_keys(email)
    driver.find_element(By.ID, "signupPassword").send_keys(password)
    driver.find_element(By.ID, "signupRepeatPassword").send_keys(password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Register')]"))
    ).click()

    success_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'alert-success')]"))
    )
    assert "registration complete" in success_alert.text.lower()