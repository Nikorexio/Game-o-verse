from selenium import webdriver
import time
import math
import os 


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)

	# Ваш код, который заполняет обязательные поля
	
	input1 = browser.find_element_by_css_selector('[name*="first"]').send_keys("AC")
	input2 = browser.find_element_by_css_selector('[name*="last"]').send_keys("AB")
	input3 = browser.find_element_by_css_selector('[name*="email"]').send_keys("aboba@bigus.fr")
	element = browser.find_element_by_css_selector('#file')
	element.send_keys(file_path)
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