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
# кликаем ОК
driver.find_element(By.XPATH, '//button[@class="button--g31Xx button__white--pn5Tx cookie-consent__submit-button"]').click()
# Открываем анкету
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/cards/svoya"]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx card-brief__button"]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx choose-application-way__continue-button"]'))).click()
# Заполняем поля анкеты
fio = driver.find_elements(By.XPATH, '//input[@class="smartInput__input--zqFgL"]')
for i in range(3):
    choose_suggestion(fio[i], 'char')

# выбираем пол:
sex = driver.find_elements(By.XPATH, '//input[@class="radio__optionInput--fSYTn"]')
random.choice(sex).click()

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
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[4]/div[2]/div/div/input')
elem.click()
slow_input(elem, '9' + str(random.randint(111111111, 999999999)))
# Email
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[4]/div[1]/div/div/div[1]/input')
slow_input(elem, 'iii@mail.com')

# Данные паспорта

elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/div/input')
elem.click()
slow_input(elem, str(random.randint(1000, 9999)))

elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/input')
elem.click()
slow_input(elem, str(random.randint(100000, 999999)))

# Дата выдачи
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div')
elem.click()
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div/div/input')
slow_input(elem, '11112000')

# Код подразделения
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/input')
for i in range(6):
    elem.send_keys(Keys.ARROW_LEFT)
elem.send_keys('1')
elem.send_keys(Keys.ARROW_DOWN)
elem.send_keys(Keys.ENTER)

#Место жительства





"""
# Coгласия
consents = driver.find_elements(By.XPATH,
                                '//button[@class="button--g31Xx button__white--pn5Tx application-debit__sign-button"]')
consents[0].click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[@class="button--g31Xx modal-consent__button-sing"]'))).click()
consents[1].click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx modal-consent__button-sing"]'))).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx application-debit__submit-button"]'))).click()
# SMS
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//input[@class="smsCodeInput__digit--O14Lj"]')))
fill_fake_sms()
# Second page - Параметры карты
# Select currency
currencies_buttons = '//button[@class="button--g31Xx button__inline--EKkD5 card-data-debit__radio-btn" or @class="button--g31Xx button__inline--EKkD5 card-data-debit__radio-btn card-data-debit__radio-btn_active"]'
currencies = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, currencies_buttons)))
chosen_currency = random.choice(currencies)
chosen_currency.click()
# Select paymentsystem
paymentsystems = driver.find_elements(By.XPATH,
                                      '//button[@class="button--g31Xx button__inline--EKkD5 card-data-debit__radio-btn card-data-debit__radio-btn__centered"]')
paymentsystem = random.choice(paymentsystems)
paymentsystem.click()
# Card category
driver.find_element(By.XPATH, '//div[@role="listbox"]').click()
categories = driver.find_elements(By.XPATH, '//li[@role="option"]')
category = categories[0]
# category = random.choice(categories)
category.click()
"""



driver.quit()
