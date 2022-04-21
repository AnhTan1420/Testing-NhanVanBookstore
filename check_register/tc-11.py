from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://nhanvan.vn/")

driver.find_element(By.XPATH, "//*[@id='header']/div[2]/div/div/div[3]/div/div[3]/a[2]").click()
driver.find_element(By.NAME, "register").click()
driver.find_element(By.NAME, "customer[last_name]").send_keys("Anh")
driver.find_element(By.NAME, "customer[first_name]").send_keys("Tan")
driver.find_element(By.XPATH, "//*[@id='radio2']").click()
time.sleep(2)
driver.find_element(By.NAME, "customer[birthday]").send_keys("12/20/2001")
driver.find_element(By.NAME, "customer[email]").send_keys("anhtan1220@gmail.com.")
driver.find_element(By.NAME, "customer[password]").send_keys("12356789")
driver.find_element(By.XPATH, "//*[@id='create_customer']/div[7]/div/input").click()
time.sleep(6)
driver.close()