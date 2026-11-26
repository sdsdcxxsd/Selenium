from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


USERNAME = "lavrovnikita1337@gmail.com"
PASSWORD = "****"


def login_to_github():
    print("Запуск браузера...")
    driver = webdriver.Chrome()

    try:
        driver.get("https://github.com/login")
        print("Страница загружена. Ищем поля...")

        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        )

        username_field.clear()
        username_field.send_keys(USERNAME)
        time.sleep(1)

        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(PASSWORD)
        time.sleep(1)


        login_button = driver.find_element(By.NAME, "commit")
        login_button.click()

        print("Кнопка входа нажата. Ждем результата...")

        time.sleep(5)

    finally:
        driver.quit()
        print("Браузер закрыт.")


if __name__ == "__main__":
    login_to_github()