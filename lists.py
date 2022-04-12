from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


try:
	link = "http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	select = Select(browser.find_element_by_tag_name("select"))


	# Ваш код, который заполняет обязательные поля
	
	f_val = browser.find_element_by_css_selector('#num1').text
	s_val = browser.find_element_by_css_selector('#num2').text
	res = int(f_val)+int(s_val)
	select.select_by_value(str(res))
	time.sleep(1)
	
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
	
	
	
	#	browser.execute_script("return arguments[0].scrollIntoView(true);", button)