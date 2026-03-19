from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

first = driver.find_element(By.XPATH, '//input[@id="searchInput"]')
print(first)

second = driver.find_element(By.XPATH, '//a[@id="js-link-box-en"]')
print(second)

third = driver.find_element(By.XPATH, '//div[@class="footer-sidebar-icon sprite svg-wikipedia_app_tile"]')
print(third)

fourth = driver.find_elements(By.CSS_SELECTOR, ".central-featured-lang")
print(len(fourth))

time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

print(driver.title)

driver.quit()