from selenium import webdriver
from selenium.webdriver.common.by import By

timeout = 3
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(timeout)

driver.get("http://10.7.27.52:81/")
#кликаем ОК
driver.find_element(By.XPATH, '//button[@class="button--g31Xx button__white--pn5Tx cookie-consent__submit-button"]').click()

# Открываем все ПК и проверяем текст
product = driver.find_element(By.XPATH, '//a[@href="/loans/special_offer"]').click()
title = driver.find_element(By.XPATH, '//h1[@class="loan-banner__h1"]')
assert title.text == 'Кредит на всё, что хочется!'
driver.back()

product = driver.find_element(By.XPATH, '//a[@href="/loans/special_offer_pens"]').click()
title = driver.find_element(By.XPATH, '//h1[@class="loan-banner__h1"]')
assert title.text == 'Пенсионный кредит от 5,5% годовых'
driver.back()

product = driver.find_element(By.XPATH, '//a[@href="/loans/bez_op"]').click()
title = driver.find_element(By.XPATH, '//h1[@class="loan-banner__h1"]')
assert title.text == 'Кредит на любые цели'
driver.back()

product = driver.find_element(By.XPATH, '//a[@href="/loans/refin"]').click()
title = driver.find_element(By.XPATH, '//h1[@class="loan-banner__h1"]')
assert title.text == 'Рефинансирование кредитов'
driver.back()

product = driver.find_element(By.XPATH, '//a[@href="/loans/pens"]')
product.click()
title = driver.find_element(By.XPATH, '//h1[@class="loan-banner__h1"]')
assert title.text == 'Кредит пенсионный'
driver.back()

# Открываем все КЗ и проверяем текст
product = driver.find_element(By.XPATH, '//a[@href="/loans/dlya_samozanyatykh/"]')
product.click()
title = driver.find_element(By.XPATH, '//h1[@class="loan-banner__h1"]')
assert title.text == 'Для самозанятых граждан'
driver.back()

product = driver.find_element(By.XPATH, '//a[@href="/loans/offer_villagers"]')
product.click()
title = driver.find_element(By.XPATH, '//h1[@class="loan-banner__h1"]')
assert title.text == 'Потребительский кредит на благоустройство для жителей села'
driver.back()

product = driver.find_element(By.XPATH, '//a[@href="/loans/gazomotornoye_toplivo"]')
product.click()
title = driver.find_element(By.XPATH, '//h1[@class="loan-banner__h1"]')
assert title.text == 'Газомоторное топливо'
driver.back()

product = driver.find_element(By.XPATH, '//a[@href="/loans/family_offer_credit"]')
product.click()
title = driver.find_element(By.XPATH, '//h1[@class="loan-banner__h1"]')
assert title.text == 'Семейное предложение'
driver.back()

# Открываем все КК и проверяем текст
product = driver.find_element(By.XPATH, '//a[@href="/cards/svoya"]')
product.click()
title = driver.find_element(By.XPATH, '//h1[@class="card-banner__h1"]')
assert title.text == 'СВОЯ кредитная карта'
driver.back()

product = driver.find_element(By.XPATH, '//a[@href="/cards/putevaya"]')
product.click()
title = driver.find_element(By.XPATH, '//h1[@class="card-banner__h1"]')
assert title.text == 'Путевая кредитная карта'
driver.back()

product = driver.find_element(By.XPATH, '//a[@href="/cards/amur"]')
product.click()
title = driver.find_element(By.XPATH, '//h1[@class="card-banner__h1"]')
assert title.text == 'Кредитная карта Амурский тигр'
driver.back()

# Открываем все ДК и проверяем текст
product = driver.find_element(By.XPATH, '//a[@href="/cards/svoya-debet"]').click()
title = driver.find_element(By.XPATH, '//h1[@class="card-banner__h1"]')
assert title.text == 'СВОЯ карта'
driver.back()

product = driver.find_element(By.XPATH, '//a[@href="/cards/amur-debet"]').click()
title = driver.find_element(By.XPATH, '//h1[@class="card-banner__h1"]')
assert title.text == 'Дебетовая карта Амурский тигр'
driver.back()

product = driver.find_element(By.XPATH, '//a[@href="/cards/pens-debet"]').click()
title = driver.find_element(By.XPATH, '//h1[@class="card-banner__h1"]')
assert title.text == 'Пенсионная карта'
driver.back()

product = driver.find_element(By.XPATH, '//a[@href="/cards/vordi-debet"]').click()
title = driver.find_element(By.XPATH, '//h1[@class="card-banner__h1"]')
assert title.text == 'Дебетовая карта РСХБ-ВОРДИ'
driver.back()

driver.quit()



