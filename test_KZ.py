import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

#Замедление ввода символов в поля
def slow_input(elem, text):
    for character in text:
        elem.send_keys(character)
        time.sleep(0.05)  # pause for 0.05 seconds

#Ввод смс кода в тестовом режиме
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
driver.implicitly_wait(timeout)
kzs = ['loans/gazomotornoye_toplivo', 'loans/dlya_samozanyatykh/', 'loans/offer_villagers']
url = 'https://portal-ui-cc.cprb.dev.rshbdev.ru/'   #'http:///10.7.27.52:81/'
driver.get(url)
# кликаем ОК
driver.find_element(By.XPATH,
                    '//button[@class="button--g31Xx button__white--pn5Tx cookie-consent__submit-button"]').click()
# Открываем кредит
driver.get(url + kzs[0])
time.sleep(2)
driver.find_element(By.XPATH,
                    '//button[@class="button--g31Xx loan-brief__button-text"]').click()
# Заполняем поля анкеты
fio = driver.find_elements(By.XPATH, '//input[@class="smartInput__input--zqFgL"]')
for i in range(3):
    choose_suggestion(fio[i], 'char')
# выбираем пол:
sex = driver.find_elements(By.XPATH, '//input[@class="radio__optionInput--fSYTn"]')
random.choice([sex[0], sex[1]]).click()
#ДР
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[5]/div/div/div/div')
elem.click()
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[5]/div/div/div/div/input')
slow_input(elem, '11111980')
#Телефон и почта
elem = driver.find_element(By.XPATH,
                           '//input[@class="smartInput__input--zqFgL phoneInput__input--SqDvP"]')
elem.click()
slow_input(elem, '9091239456')
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[4]/div[2]/div/div/div[1]/input')
slow_input(elem, 'iii@mail.com')

driver.quit()