import random
import time

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

driver.get("http://10.7.27.52:81/")
time.sleep(2)
# кликаем ОК
driver.find_element(By.XPATH, '//button[@class="button--g31Xx button__white--pn5Tx cookie-consent__submit-button"]').click()
#driver.find_element("link text", "Понятно")
# Открываем анкету
driver.find_element(By.XPATH, '//a[@href="/cards/svoya"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//button[@class="button--g31Xx card-brief__button"]').click()
driver.find_element(By.XPATH, '//button[@class="button--g31Xx choose-application-way__continue-button"]').click()
time.sleep(3)
# Заполняем поля анкеты
elem = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/div/input')
choose_suggestion(elem, 'char')
time.sleep(3)
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/input')
choose_suggestion(elem, 'char')

elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div/div/input')
choose_suggestion(elem, 'char')

# выбираем пол:
female = driver.find_element(By.XPATH,
                             '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/button[1]/div/label/div/input')
male = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/button[2]/div/label/div/input')
sex = [female, male]
random.choice(sex).click()

# Дата рождения
elem = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[3]/div[1]/div/div')
elem.click()
elem = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[3]/div[1]/div/div/div/input')
slow_input(elem, '11111980')
#Место рождения
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[3]/div[2]/div/div/input')
elem.click()
slow_input(elem, 'Рим')
#Телефон
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[4]/div[2]/div/div/input')
elem.click()
slow_input(elem, '9091239456')
#email
elem = driver.find_element(By.XPATH,
                           '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[4]/div[1]/div/div/div/input')
slow_input(elem, 'iii@mail.com')
"""
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
elem = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div/div')
elem.click()
elem = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div[1]/div/input')
slow_input(elem, '11112000')

# Код подразделения
elem = driver.find_element(By.XPATH,
                    '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div/div[1]/input')
time.sleep(1)
for i in range(6):
    elem.send_keys(Keys.ARROW_LEFT)
elem.send_keys('1')
time.sleep(1)
elem.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
elem.send_keys(Keys.ENTER)
#choose_suggestion(elem, 'digit')
elem = driver.find_element(By.XPATH,
                    '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/div/div[1]')
#Coгласия
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div[1]/div[3]/div/div/div[2]/div/div[2]/div[1]/div[1]/button').click()
time.sleep(1)
driver.find_element(By.XPATH,
                    '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]').click()
time.sleep(1)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div[1]/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/button').click()
time.sleep(1)
driver.find_element(By.XPATH,
                    '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]').click()

driver.find_element(By.XPATH,
                    '//*[@id="root"]/div[1]/div[3]/div/div/div[2]/div/div[2]/div[3]').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[3]/div/input[1]').send_keys('1')
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[3]/div/input[2]').send_keys('2')
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[3]/div/input[3]').send_keys('3')
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[3]/div/input[4]').send_keys('4')

driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[6]/div[2]/button').click()

#Second page

#Select currency
time.sleep(4)
currencies = driver.find_elements(By.XPATH, '//button[@class="button--g31Xx button__inline--EKkD5 card-data-debit__radio-btn"]')
chosen_currency = random.choice(currencies)
chosen_currency.click()
time.sleep(2)
#Select paymentsystem
paymentsystems = driver.find_elements(By.XPATH, '//button[@class="button--g31Xx button__inline--EKkD5 card-data-debit__radio-btn card-data-debit__radio-btn__centered"]')
print(paymentsystems.count())
paymentsystem = random.choice(paymentsystems)
paymentsystem.click()


"""


driver.quit()
