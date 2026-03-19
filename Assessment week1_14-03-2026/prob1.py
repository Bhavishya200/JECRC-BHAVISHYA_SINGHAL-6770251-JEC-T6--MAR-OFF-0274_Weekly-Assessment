from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

first = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
print(first)

second = driver.find_element(By.CSS_SELECTOR, "input[id='password']")
print(second)

third = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
print(third)

fourth = driver.find_element(By.CSS_SELECTOR, "#page-footer a")
print(fourth)