from selenium import webdriver
import time


websites = [
    "https://www.thesouledstore.com",
    "https://www.nike.com",
    "https://www.amazon.in",
    "https://www.python.org"
]

driver = webdriver.Chrome()

for site in websites:
    driver.get(site)
    time.sleep(3)
    print("Website:", site)
    print("Title:", driver.title)
    print("----------------------")

driver.quit()