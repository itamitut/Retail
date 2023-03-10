import random
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# Выбирает из подсказок рандомную:
def choose_suggestion(elem, type):
    alpha = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Х',
             'Ч', 'Э', 'Ю', 'Я']
    elem.click()
    if type == 'char':
        elem.send_keys(random.choice(alpha))
        time.sleep(1)
    else:
        elem.send_keys(chr(random.randint(0, 9)))

    for i in range(random.randint(1, 10)):
        elem.send_keys(Keys.DOWN)
    elem.send_keys(Keys.ENTER)

# Замедление ввода символов в поля
def slow_input(elem, text):
    for character in text:
        elem.send_keys(character)
        time.sleep(0.1)  # pause for 0.2 seconds

# Ввод смс кода в тестовом режиме
def fill_fake_sms():
    sms_digits = driver.find_elements(By.XPATH, '//input[@class="smsCodeInput__digit--O14Lj"]')
    sms_digits[0].send_keys('1')
    sms_digits[1].send_keys('2')
    sms_digits[2].send_keys('3')
    sms_digits[3].send_keys('4')
    driver.find_element(By.XPATH, '//button[@class="button--g31Xx sms-confirmation__button"]').click()
    time.sleep(2)

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://portal-ui-cc.cprb.dev.rshbdev.ru")
#"https://portal-ui-cc.cprb.rshbdev.ru/"
# кликаем ОК
driver.find_element(By.XPATH, '//button[@class="button--g31Xx button__white--pn5Tx cookie-consent__submit-button"]').click()


# Открываем анкету
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/cards/svoya"]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx card-brief__button"]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx choose-application-way__continue-button"]'))).click()

#Дата регистрации
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/div/div[1]/div')
elem.click()
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/div/div[1]/div/input')
elem.click()
slow_input(elem, '11112000')
elem.click()
#Checkbox
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[3]/div[2]/div[4]/label/div/input').click()

time.sleep(5)
driver.quit()
