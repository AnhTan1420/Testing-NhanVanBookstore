from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://nhanvan.vn/")

driver.find_element(By.XPATH,"//header/div[@id='header']/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/a[1]").click()
driver.find_element(By.NAME,"customer[email]").send_keys("")
driver.find_element(By.NAME,"customer[password]").send_keys("17092001")
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='customer_login']/div[3]/div[1]/button").click()
TB = driver.find_element(By.NAME,"customer[email]").get_attribute('validationMessage')
print(TB)

time.sleep(3)
driver.close()