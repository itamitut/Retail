import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Выбирает из подсказок рандомную:
def choose_suggestion(elem, type):
    elem.click()
    if type == 'char':
        elem.send_keys(chr(random.randint(ord('А'), ord('Я'))))
    else:
        elem.send_keys(chr(random.randint(0, 9)))

    for i in range(random.randint(1, 10)):
        elem.send_keys(Keys.DOWN)
    elem.send_keys(Keys.ENTER)


def slow_input(elem, text):
    for character in text:
        elem.send_keys(character)
        time.sleep(0.1)  # pause for 0.2 seconds


timeout = 3
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(timeout)

driver.get("https://portal-ui-cc.cprb.dev.rshbdev.ru/")
# Кликаем ОК
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx button__white--pn5Tx cookie-consent__submit-button"]'))).click()
driver.quit()
#actions = ActionChains(driver)
#actions.move_to_element(product).perform()