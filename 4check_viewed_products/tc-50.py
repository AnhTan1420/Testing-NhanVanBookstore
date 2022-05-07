from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://nhanvan.vn/")

    # ĐĂNG NHẬP
    driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/div[3]/div/div[3]/a[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="customer_email"]').send_keys('anhtan123@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="customer_password"]').send_keys('12356789')
    driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[3]/div[1]/button').submit()
    time.sleep(3)

    # TÌM KIẾM ĐỂ XEM SẢN PHẨM
    driver.find_element(By.XPATH, '//*[@id="inputSearchAuto-dt"]').send_keys('đắc nhân tâm')
    driver.find_element(By.XPATH, '//*[@id="searchsubmit"]').submit()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div/div[3]/div/div[2]/div[1]/h3/a').click()
    time.sleep(3)

    # MỞ DANH SÁCH SẢN PHẨM ĐÃ XEM
    driver.get('https://nhanvan.vn/account')
    time.sleep(3)
    driver.find_element(By.XPATH,
                        '//*[@id="siêu-thị-sách-&-tiện-ích-nhân-văn"]/div[1]/div[1]/div/main/div/div[2]/div/div[1]/div/div/div/ul/li[4]/a').click()
    time.sleep(3)

    # KIỂM TRA HIỂN THỊ TÊN DANH SÁCH
    print(driver.find_element(By.XPATH,
                              '//*[@id="siêu-thị-sách-&-tiện-ích-nhân-văn"]/div[1]/div[1]/div/main/div/div[2]/div/div/div/div[1]/h1').text)

    # KIỂM TRA HIỂN THỊ ĐÚNG THÔNG TIN SẢN PHẨM (ẢNH, TÊN, GIÁ)
    recentlySeen = driver.find_elements(By.CSS_SELECTOR, 'div.item-featured')
    for itemInfo in recentlySeen:
        image = itemInfo.find_element(By.CSS_SELECTOR, 'div.featured-img>a>img').get_attribute('src')
        print(image)
        print(itemInfo.text)
        print('------------------------')
except:
    print('Oops... ERROR, please run again.')

time.sleep(5)
driver.close()
