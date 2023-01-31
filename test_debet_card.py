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


timeout = 5
driver = webdriver.Chrome()
driver.maximize_window()
#wait = WebDriverWait(driver, 10)  # seconds
#driver.implicitly_wait(timeout)
debet_cards = ['cards/svoya-debet', 'cards/amur-debet', 'cards/pens-debet']
url = 'https://portal-ui-cc.cprb.dev.rshbdev.ru/' #'http://10.7.27.52:81/'

driver.get(url)
# кликаем ОК
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx button__white--pn5Tx cookie-consent__submit-button"]'))).click()

for debet_card in debet_cards:
    driver.get(url + debet_card)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx card-brief__button"]'))).click()

    # Заполняем поля анкеты
    fio = driver.find_elements(By.XPATH, '//input[@class="smartInput__input--zqFgL"]')
    for i in range(3):
        choose_suggestion(fio[i], 'char')
    # выбираем пол:
    sex = driver.find_elements(By.XPATH, '//input[@class="radio__optionInput--fSYTn"]')
    random.choice(sex).click()
    # Дата рождения
    elem = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div[1]')
    elem.click()
    elem = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div/input')
    slow_input(elem, '11111980')
    #Телефон
    elem = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[4]/div[1]/div/div[1]/input')
    elem.click()
    slow_input(elem, '9' + str(random.randint(111111111, 999999999)))
    # Email
    elem = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[4]/div[2]/div/div/div[1]/input')
    slow_input(elem, 'iii@mail.com')

    # Данные паспорта

    elem = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/input')
    elem.click()
    slow_input(elem, str(random.randint(1000, 9999)))

    elem = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/input')
    elem.click()
    slow_input(elem, str(random.randint(100000, 999999)))

    # Дата выдачи
    elem = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div/div')
    elem.click()
    elem = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div[1]/div/input')
    slow_input(elem, '11112000')

    # Код подразделения
    elem = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div/div[1]/input')
    for i in range(6):
        elem.send_keys(Keys.ARROW_LEFT)
    elem.send_keys('1')
    elem.send_keys(Keys.ARROW_DOWN)
    elem.send_keys(Keys.ENTER)
    # choose_suggestion(elem, 'digit')
    elem = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/div/div[1]')
    # Coгласия
    consents = driver.find_elements(By.XPATH, '//button[@class="button--g31Xx button__white--pn5Tx application-debit__sign-button"]')
    consents[0].click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@class="button--g31Xx modal-consent__button-sing"]'))).click()
    consents[1].click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx modal-consent__button-sing"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx application-debit__submit-button"]'))).click()
    #SMS
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//input[@class="smsCodeInput__digit--O14Lj"]')))
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

    # Embossed fio
    wait = WebDriverWait(driver, 10)  # seconds
    # wait.until(EC.visibility_of(driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div/div/input')))

    elems = driver.find_elements(By.XPATH, '//input[@class="smartInput__input--zqFgL"]')
    elems[0].click()
    if len(elems) == 3:
        slow_input(elems[0], 'RALF')
        slow_input(elems[1], 'HGRAHKJHKHHKJHKH')
        slow_input(elems[2], 'КОД')
    else:
        slow_input(elems[0], 'RALF GRAHKJHKHHKJHKH')
        slow_input(elems[1], 'КОД')
    # CHECK_word

    time.sleep(3)
    # Click Далее
    driver.find_element(By.XPATH, '//button[@class="button--g31Xx applicationWidgetButtons__button"]').click()
    time.sleep(1)
    # 3d page
    driver.find_element(By.XPATH, '//input[@class="smartInput__input--zqFgL"]').send_keys('Рим')
    driver.find_element(By.XPATH, '//button[@class="button--g31Xx applicationWidgetButtons__button"]').click()
    # SNILS&INN

    driver.find_element(By.XPATH, '//button[@class="button--g31Xx applicationWidgetButtons__button"]').click()
    time.sleep(1)
    # Address
    radiobuttons = driver.find_elements(By.XPATH, '//input[@class="radio__optionInput--fSYTn"]')
    radiobuttons[1].click()
    radiobuttons[3].click()

    address_forms = driver.find_elements(By.XPATH, '//input[@class="smartInput__input--zqFgL"]')
    choose_suggestion(address_forms[0], 'char')
    choose_suggestion(address_forms[1], 'char')
    choose_suggestion(address_forms[3], 'char')
    address_forms[4].send_keys('1')
    slow_input(address_forms[8], '431440')
    driver.find_element(By.XPATH,
                        '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div[6]/div[2]/label/div/input').click()
    # Date
    elem = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]')
    elem.click()
    elem = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/input')
    slow_input(elem, '10102000')
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div[2]/div[4]/div[2]/button').click()

    # 4th page

    branches = driver.find_elements(By.XPATH, '//input[@class="content__input--Tmhjf"]')
    time.sleep(1)
    branches[0].click()
    branches[0].send_keys('вл')
    branches[0].send_keys(Keys.DOWN)
    branches[0].send_keys(Keys.ENTER)
    branches[1].click()
    branches[1].send_keys('ковров')
    branches[1].send_keys(Keys.DOWN)
    branches[1].send_keys(Keys.ENTER)
    # Согласия
    consents = driver.find_elements(By.XPATH, '//button[@class="button--g31Xx button__white--pn5Tx consents-actions-debit__sign-button"]')
    time.sleep(1)
    consents[0].click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx modal-consent__button-sing"]'))).click()
    consents[1].click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx modal-consent__button-sing"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx consents-actions-debit__submit-button"]'))).click()
    # SMS
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//input[@class="smsCodeInput__digit--O14Lj"]')))
    fill_fake_sms()


#    assert driver.find_element(By.XPATH, '//div[@class="modal-sent__title"]').text == 'Заявка отправлена'
driver.quit()
