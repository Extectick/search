from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("http://www.ya.ru")

time.sleep(2)
elem = driver.find_element_by_id("text")
elem.clear()
elem.send_keys("котики картинки")
elem.send_keys(Keys.RETURN)
time.sleep(4)
driver.close()