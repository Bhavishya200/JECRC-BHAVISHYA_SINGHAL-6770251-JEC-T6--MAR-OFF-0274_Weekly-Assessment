from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationexercise.com/login")

wait = WebDriverWait(driver, 10)


wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("iocniwoef")

driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys('vwebv@gmail.com')

wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-qa="signup-button"]'))).click()

wait.until(EC.visibility_of_element_located((By.ID, "id_gender1")))

driver.find_element(By.ID, "id_gender1").click()

newsletter = driver.find_element(By.ID, "newsletter")
offers = driver.find_element(By.ID, "optin")

newsletter.click()
offers.click()

print(newsletter.get_attribute("checked"))
print(offers.get_attribute("checked"))


sleep(5)
driver.quit()