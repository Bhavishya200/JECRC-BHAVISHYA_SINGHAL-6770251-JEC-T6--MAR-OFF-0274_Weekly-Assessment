from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com")


wait = WebDriverWait(driver, 10)


search = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'gLFyf')))

search.send_keys("Selenium Python")


sugg = wait.until( EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li")))

for s in sugg:
    print(s.text)

sugg[3].click()

sleep(5)
driver.quit()