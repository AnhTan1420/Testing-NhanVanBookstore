from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://nhanvan.vn/")

driver.find_element(By.NAME,"q").send_keys("  Đắc nhân tâm")
driver.find_element(By.XPATH,"//*[@id='searchsubmit']").submit()
driver.implicitly_wait(7)

results=driver.find_elements(By.CSS_SELECTOR,'.search-list-results .pro-loop.grid-item .product-block .product-detail .box-pro-detail h3')
for item in results:
    content= item.find_element(By.TAG_NAME,'a')
    print(content.text)
    print(content.get_attribute('href'))
    print('-------------------')
time.sleep(3)
driver.close()
