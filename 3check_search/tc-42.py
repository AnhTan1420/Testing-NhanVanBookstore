from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://nhanvan.vn/")

driver.find_element(By.NAME,"q").send_keys("")
driver.find_element(By.XPATH,"//*[@id='searchsubmit']").click()
results= driver.find_element(By.NAME,"q").get_attribute('validationMessage')
print(results)
if results=='Please fill out this field.':
    print('Passed')
else:
    print('Failed')
time.sleep(3)
driver.close()