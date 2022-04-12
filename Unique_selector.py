from selenium import webdriver
import time
import math


try:
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)

	# Ваш код, который заполняет обязательные поля
	
	x = browser.find_element_by_css_selector("#treasure").get_attribute("valuex")
	val = math.log(abs(12*math.sin(int(x))))
	input1 = browser.find_element_by_css_selector('#answer')
	input1.send_keys(str(val))
	checkbox = browser.find_element_by_css_selector('#robotCheckbox')
	checkbox.click()
	radio = browser.find_element_by_css_selector('#robotsRule')
	radio.click()
	time.sleep(3)

	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
	time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()