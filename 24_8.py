from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    x=(int(x))
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    # Нажать на кнопку Book
    button = browser.find_element(By.CSS_SELECTOR, 'button[id="book"]').click()
    # Дождаться появления капчи
    # Считать значение переменной х
    x_elem = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = x_elem.text
    # Посчитать математическую функцию от x
    f = calc(x)
    # Ввести ответ в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control')
    input1.send_keys(f)
    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


