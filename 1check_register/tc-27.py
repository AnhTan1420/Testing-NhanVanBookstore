from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://nhanvan.vn/")
driver.find_element(By.XPATH, "//*[@id='header']/div[2]/div/div/div[3]/div/div[3]/a[2]").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div[2]/div/div/div/div[2]/ul/li[2]/input").click()
time.sleep(3)
driver.find_element(By.NAME, "phone_number").send_keys("0176 378 37,9")
driver.find_element(By.XPATH, "//*[@id='phone-auth-submit']").click()

time.sleep(6)
driver.close()
