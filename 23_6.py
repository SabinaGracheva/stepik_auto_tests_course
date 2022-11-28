from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    x=(int(x))
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    # Открыть страницу
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button").click()
    # Переключить на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # Считать значение переменной х
    x_elem = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = x_elem.text
    # Посчитать математическую функцию от x
    f = calc(x)
    # Ввести ответ в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control')
    input1.send_keys(f)
    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


