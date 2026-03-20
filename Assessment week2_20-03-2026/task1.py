from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.amazon.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
sleep(3)
if "Amazon" in driver.title:
    print("title: verified")
else:
    print("title: not verified")

if 'amazon.com' in driver.current_url:
    print("url :Verified")
else:
    print("url: not verified")

dropdown = driver.find_element(By.ID, "searchDropdownBox")
select = Select(dropdown)
select.select_by_visible_text("Books")

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("harry potter",Keys.ENTER)

products = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]/span')))


for p in products[:5]:
    print(p.text)

products[0].click()

driver.quit()