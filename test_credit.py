# For loans/bez_op
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Выбирает из подсказок рандомную:
def choose_suggestion(elem, type):
    alpha = ['А', 'Б', 'В', 'Г', 'Д', 'Е',  'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Х',
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
driver.find_element(By.XPATH,
                    '//button[@class="button--g31Xx button__white--pn5Tx cookie-consent__submit-button"]').click()

# Параметры кредита
loan_sum = '99990'  # Сумма от 30 000 до 3 000 000 кратно 10
loan_term = '36'  # Cрок в мес от 13 до 60
is_rshb = 0  # Получаю зп на счет в Рсхб
insurance = 1  # Комплексная страховая защита

# Открываем анкету
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/loans/bez_op"]'))).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx loan-brief__button-text"]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[@class="button--g31Xx choose-application-way__continue-button"]'))).click()

# Вводим параметры кредита
elems = driver.find_elements(By.XPATH, '//input[@class="slider__input--K6L3y"]')
elems[0].clear()
elems[0].click()
elems[0].send_keys(loan_sum)
elems[1].click()
elems[1].clear()
slow_input(elems[1], loan_term)

# Если надо указать зп клиент раскомментировать
# driver.find_element(By.XPATH, '//input[@class="checkbox__input--GTFhJ"]').click()
# Персональные данные
# Заполняем поля анкеты
fio = driver.find_elements(By.XPATH, '//input[@class="smartInput__input--zqFgL"]')
for i in range(3):
    choose_suggestion(fio[i], 'char')

# выбираем пол:
sex = driver.find_elements(By.XPATH, '//input[@class="radio__optionInput--fSYTn"]')[:2]
random.choice(sex).click()
# Место рождения
fio[3].send_keys('Рим')
# ДР через календарь
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="content__control--U7mF7"]'))).click()
year_arrow = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="date__leftDoubleArrow--uitfe"]')))
month_arrow = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="date__leftArrow--dfVtT"]')))
for i in range(random.randint(21, 63)):
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
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div[2]/div/div[1]/input')
elem.click()
slow_input(elem, '9' + str(random.randint(111111111, 999999999)))
# Email
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/input')
slow_input(elem, 'iii@mail.com')

# Данные паспорта

elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[3]/div[2]/div/div[1]/div[1]/div/div/input')
elem.click()
slow_input(elem, str(random.randint(1000, 9999)))

elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[3]/div[2]/div/div[1]/div[2]/div/div/input')
elem.click()
slow_input(elem, str(random.randint(100000, 999999)))

# Дата выдачи
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[3]/div[2]/div/div[1]/div[3]/div/div[1]/div').click()
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[3]/div[2]/div/div[1]/div[3]/div/div[1]/div/input')
slow_input(elem, '11112000')

# Код подразделения
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div').click()
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div/input')
elem.click()
for i in range(6):
    elem.send_keys(Keys.ARROW_LEFT)
elem.send_keys('1')
elem.send_keys(Keys.ARROW_DOWN)
elem.send_keys(Keys.ENTER)

# Место жительства
# Выбираем заполнение полями
driver.find_elements(By.XPATH, '//input[@class="radio__optionInput--fSYTn"]')[3].click()
address_fields = driver.find_elements(By.XPATH, '//input[@class="smartInput__input--zqFgL"]')
choose_suggestion(address_fields[0], 'char')
choose_suggestion(address_fields[2], 'char')
choose_suggestion(address_fields[3], 'char')
address_fields[4].send_keys('1')
slow_input(address_fields[8], '123456')
# Дата регистрации
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[4]/div[2]/div[2]/div[2]/div/div/div/div').click()
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[4]/div[2]/div[2]/div[2]/div/div/div/div/input')
slow_input(elem, '11112001')
address_fields[8].click()
# Checkbox
checkbox = driver.find_elements(By.XPATH, '//input[@class="checkbox__input--GTFhJ"]')
checkbox[3].click()
# Среднемесячный доход
address_fields[10].send_keys('100000')
# Отделение Банка
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
# Coгласия
consents = driver.find_elements(By.XPATH,
                                '//button[@class="button--g31Xx button__white--pn5Tx application-short__sign-button"]')
consents[0].click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[@class="button--g31Xx modal-consent__button-sing"]'))).click()
consents[1].click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[@class="button--g31Xx modal-consent__button-sing"]'))).click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx application-short__submit-button"]'))).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//input[@class="smsCodeInput__digit--O14Lj"]')))
# SMS
fill_fake_sms()
# Согласие БКИ
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx modalBki__button-continue"]'))).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx modal-consent__button-sing"]'))).click()
time.sleep(2)
fill_fake_sms()
# Продолжить заполнение
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx modal-sent__button-continue"]'))).click()
# Second page
# Персональные данные
# Образование
elem = driver.find_element(By.XPATH, '//div[@class="content--CSXGL"]')
elem.click()
elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, '//button[@class="button--g31Xx applicationWidgetButtons__button"]').click()
time.sleep(1)
# Семейное положение
elem = driver.find_element(By.XPATH, '//div[@class="content--CSXGL"]')
elem.click()
elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.ENTER)
time.sleep(1)
elem = driver.find_element(By.XPATH, '//input[@class="smartInput__input--zqFgL"]')
elem.send_keys('1')
driver.find_element(By.XPATH, '//button[@class="button--g31Xx applicationWidgetButtons__button"]').click()
time.sleep(1)
# Документы
elem = driver.find_element(By.XPATH, '//input[@class="smartInput__input--zqFgL"]')
slow_input(elem, '26179646208')
driver.find_element(By.XPATH, '//button[@class="button--g31Xx applicationWidgetButtons__button"]').click()
time.sleep(1)
# Адрес проживания
elem = driver.find_element(By.XPATH, '//div[@class="content--CSXGL"]')
elem.click()
elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//button[@class="button--g31Xx applicationWidgetButtons__button"]').click()
time.sleep(1)
# Контакные данные
driver.find_element(By.XPATH, '//button[@class="button--g31Xx applicationWidgetButtons__button"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//button[@class="button--g31Xx applicationWidgetButtons__button"]').click()

# Информация о трудоустройстве
elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="content--CSXGL"]')))
elem.click()
elem.send_keys(Keys.ENTER)
elem = driver.find_element(By.XPATH, '//input[@class="smartInput__input--zqFgL"]')
slow_input(elem, 'Россельхозбанк')
elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//button[@class="button--g31Xx applicationWidgetButtons__button"]').click()
time.sleep(1)
# Контакты работодателя
driver.find_element(By.XPATH, '//button[@class="button--g31Xx applicationWidgetButtons__button"]').click()
time.sleep(1)
# Информация о должности и стаже
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div[2]/div[1]/div[1]/div/div/div/div/div'))).click()
elem = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div[2]/div[1]/div[1]/div/div/div/div/div/input')
slow_input(elem, '11112000')
#Кликаем Общий лет, что бы закрыть календарь
forms = driver.find_elements(By.XPATH, '//input[@type="text"]')
forms[2].click()
# Должность  и стаж
elem = driver.find_element(By.XPATH, '//div[@role="listbox"]')
elem.click()
elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.ENTER)

forms[1].send_keys('5')
forms[2].send_keys('25')
forms[3].send_keys('5')
forms[4].send_keys('1')

driver.find_element(By.XPATH, '//button[@class="button--g31Xx applicationWidgetButtons__button"]').click()
time.sleep(2)
# Информация о доходах
elem = driver.find_element(By.XPATH, '//div[@class="content--CSXGL"]')
elem.click()
elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.ENTER)

elems = driver.find_elements(By.XPATH, '//input[@class="smartInput__input--zqFgL"]')
slow_input(elems[0], '100000')
slow_input(elems[1], '10000')
driver.find_element(By.XPATH, '//button[@class="button--g31Xx applicationWidgetButtons__button"]').click()
# Документы заемщика
# Согласие
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//button[@class="button--g31Xx button__white--pn5Tx applicationActions__signButton"]'))).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx modal-consent__button-sing"]'))).click()
# Ознакомится и отправить
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="button--g31Xx applicationActions__submitButton"]'))).click()
time.sleep(2)

# SMS
fill_fake_sms()
# Assert result
message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="modal-sent__title"]')))
# assert message.text == 'Заявка успешно отправлена'
driver.get("https://portal-ui-cc.cprb.dev.rshbdev.ru")

time.sleep(3)
driver.quit()
