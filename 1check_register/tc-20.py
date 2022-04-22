from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://nhanvan.vn/")
try:

    driver.find_element(By.XPATH, "//*[@id='header']/div[2]/div/div/div[3]/div/div[3]/a[2]").click()
    driver.find_element(By.NAME, "register").click()
    driver.find_element(By.NAME, "customer[last_name]").send_keys("Nguyễn")
    driver.find_element(By.NAME, "customer[first_name]").send_keys("Tran")
    driver.find_element(By.XPATH, "//*[@id='radio2']").click()
    time.sleep(3)
    driver.find_element(By.NAME, "customer[birthday]").send_keys("3/2/2000")
    driver.find_element(By.NAME, "customer[email]").send_keys("mama11011@gmail.com")
    driver.find_element(By.NAME, "customer[password]").send_keys("1234")

    driver.find_element(By.XPATH, "//*[@id='create_customer']/div[7]/div/input").click()
    time.sleep(3)
    TB = driver.find_element(By.XPATH, "//*[@id='create_customer']/div[1]/ul/li").text

    print(TB)
    if TB == "Mật khẩu quá ngắn (tối thiểu 5 ký tự).":
        print("Passed")
    else:
        print("Failed")
except NoSuchElementException:
    print("Loi ngoai le, vui long chay lai lan nua!")

time.sleep(6)
driver.close()
