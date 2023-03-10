import random
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
urls = ["https://portal-ui-cc.cprb.dev.rshbdev.ru/", "https://portal-ui-cc.cprb.rshbdev.ru/", "https://retail.rshb.ru/"]
#
for url in urls:
    driver.get(url)
    #кликаем ОК
    driver.find_element(By.XPATH, '//button[@class="button--g31Xx button__white--pn5Tx cookie-consent__submit-button"]').click()

    # Открываем все ПК и проверяем текст

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/loans/bez_op")]'))).click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="loan-banner__h1"]')))
    assert title.text == 'Кредит на любые цели'
    driver.back()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/loans/refin")]'))).click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="loan-banner__h1"]')))
    assert title.text == 'Рефинансирование кредитов'
    driver.back()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/loans/pens")]'))).click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="loan-banner__h1"]')))
    assert title.text == 'Кредит пенсионный'
    driver.back()

    # Открываем все КЗ и проверяем текст
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/loans/dlya_samozanyatykh")]'))).click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="loan-banner__h1"]')))
    assert title.text == 'Для самозанятых граждан'
    driver.back()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/loans/offer_villagers")]'))).click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="loan-banner__h1"]')))
    assert title.text == 'Потребительский кредит на благоустройство для жителей села'
    driver.back()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/loans/gazomotornoye_toplivo")]'))).click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="loan-banner__h1"]')))
    assert title.text == 'Газомоторное топливо'
    driver.back()

    # Открываем все КК и проверяем текст
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/cards/svoya")]'))).click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="card-banner__h1"]'))) 
    assert title.text == 'СВОЯ кредитная карта'
    driver.back()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/cards/amur")]'))).click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="card-banner__h1"]'))) 
    assert title.text == 'Кредитная карта Амурский тигр'
    driver.back()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/cards/putevaya")]'))).click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="card-banner__h1"]'))) 
    assert title.text == 'Путевая кредитная карта'
    driver.back()

    # Открываем все ДК и проверяем текст
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/cards/svoya-debet")]'))).click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="card-banner__h1"]'))) 
    assert title.text == 'СВОЯ карта'
    driver.back()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/cards/amur-debet")]'))).click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="card-banner__h1"]'))) 
    assert title.text == 'Дебетовая карта Амурский тигр'
    driver.back()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/cards/pens-debet")]'))).click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="card-banner__h1"]'))) 
    assert title.text == 'Пенсионная карта'
    driver.back()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/cards/vordi-debet")]'))).click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="card-banner__h1"]'))) 
    assert title.text == 'Дебетовая карта РСХБ-ВОРДИ'
    driver.back()
driver.quit()




