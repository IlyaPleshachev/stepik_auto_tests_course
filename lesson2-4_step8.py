from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = browser.find_element_by_id("book")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button.click()


x = browser.find_element_by_css_selector("#input_value").text
print(x)
   
itog = str(math.log(abs(12 * math.sin(int(x)))))
print(itog)
    
button = browser.find_element_by_css_selector("#solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

input1 = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(itog)

button.click()