from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'https://www.github.com'
driver.get(url)
time.sleep(1)
driver.maximize_window()
driver.save_screenshot('github.com-homepage.png')
url = 'https://www.github.com/mumudgn/'
driver.get(url)
print(driver.title)
time.sleep(2)
driver.back()
time.sleep(3)
driver.close()
