import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Выбирает из подсказок рандомную:
def choose_suggestion(elem, type):
    elem.click()
    if type == 'char':
        elem.send_keys(chr(random.randint(ord('А'), ord('Я'))))
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
        time.sleep(0.05)  # pause for 0.05 seconds


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
kzs = ['loans/gazomotornoye_toplivo', 'loans/dlya_samozanyatykh/', 'loans/offer_villagers']
url = 'https://portal-ui-cc.cprb.dev.rshbdev.ru/'  # 'http:///10.7.27.52:81/'
driver.get(url)
# кликаем ОК
driver.find_element(By.XPATH,
                    '//button[@class="button--g31Xx button__white--pn5Tx cookie-consent__submit-button"]').click()
for kz in kzs:
    # Открываем кредит
    driver.get(url + kz)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx loan-brief__button-text"]'))).click()
    # Заполняем поля анкеты
    fio = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//input[@class="smartInput__input--zqFgL"]')))
    for i in range(3):
        choose_suggestion(fio[i], 'char')
    # ДР через календарь
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="content__control--U7mF7"]'))).click()
    year_arrow = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="date__leftDoubleArrow--uitfe"]')))
    month_arrow = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="date__leftArrow--dfVtT"]')))
    for i in range(random.randint(21, 64)):
        year_arrow.click()
        time.sleep(0.05)  # pause for 0.05 secondsfor i in range(random.randint(21, 65)):
    for i in range(random.randint(0, 13)):
        month_arrow.click()
        time.sleep(0.05)  # pause for 0.05 seconds

    dates = driver.find_elements(By.XPATH,
                                 '//li[@class="date__listItem--y10uz"]')
    date = random.choice(dates)
    date.click()
    # Телефон
    elem = driver.find_element(By.XPATH,
                               '//input[@class="smartInput__input--zqFgL phoneInput__input--SqDvP"]')
    elem.click()
    slow_input(elem, '9' + str(random.randint(111111111, 999999999)))
    # Email
    elem = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div/div[4]/div[2]/div/div/div/input')
    slow_input(elem, 'iii@mail.com')
    # Согласия
    driver.find_element(By.XPATH,
                        '//button[@class="button--g31Xx button__white--pn5Tx application_special_credit__sign_button"]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@class="button--g31Xx modal-consent__button-sing"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@class="button--g31Xx application_special_credit__submit_button"]'))).click()
    #SMS
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//input[@class="smsCodeInput__digit--O14Lj"]')))
    fill_fake_sms()
    #Check result
    message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="modal-process__header"]'))).text
    assert message == 'Мы получили вашу заявку и перезвоним в ближайшее время'
    driver.find_element(By.XPATH,
                        '//button[@class="button--g31Xx modal-process__apply-button"]').click()
driver.quit()
