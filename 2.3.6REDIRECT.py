from selenium import webdriver
import time
import math
import os 


try:
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	#переключение на новое окно
	new = browser.window_handles[1]
	browser.switch_to.window(new)
	time.sleep(1)
	
	x = browser.find_element_by_css_selector("#input_value").text
	val = math.log(abs(12*math.sin(int(x))))
	
	input1 = browser.find_element_by_css_selector('#answer').send_keys(str(val))
	
	button = browser.find_element_by_css_selector("button.btn")
	button.click()	
	time.sleep(1)
	
	

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
	time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()