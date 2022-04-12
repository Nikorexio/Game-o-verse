from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


try:
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	
	browser.get(link)
	button = browser.find_element_by_css_selector("button.btn")
	price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
	button.click()
	
	x = browser.find_element_by_css_selector("#input_value").text
	val = math.log(abs(12*math.sin(int(x))))
	input1 = browser.find_element_by_css_selector("#answer").send_keys(str(val))
	submit = browser.find_element_by_css_selector("#solve").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()