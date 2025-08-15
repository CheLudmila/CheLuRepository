from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
import time

# Запуск браузера
service = Service()  # Якщо chromedriver в PATH
driver = webdriver.Chrome(service=service)

try:
    # Відкриваємо сторінку
    driver.get("http://localhost:8000/dz.html")
    driver.maximize_window()

    # --- Робота з першим фреймом ---
    driver.switch_to.frame("frame1")  # Переходимо у frame1
    input1 = driver.find_element(By.ID, "input1")
    input1.send_keys("Frame1_Secret")
    driver.find_element(By.XPATH, "//button[text()='Перевірити']").click()

    # Чекаємо та перевіряємо alert
    alert = Alert(driver)
    time.sleep(1)
    assert alert.text == "Верифікація пройшла успішно!"
    alert.accept()  # Закриваємо вікно

    # Повертаємось у головний контент
    driver.switch_to.default_content()

    # --- Робота з другим фреймом ---
    driver.switch_to.frame("frame2")
    input2 = driver.find_element(By.ID, "input2")
    input2.send_keys("Frame2_Secret")
    driver.find_element(By.XPATH, "//button[text()='Перевірити']").click()

    alert = Alert(driver)
    time.sleep(1)
    assert alert.text == "Верифікація пройшла успішно!"
    alert.accept()

    print("✅ Перевірка обох фреймів пройдена успішно!")

finally:
    time.sleep(2)
    driver.quit()