import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-incognito")
driver = webdriver.Chrome(executable_path='/home/sysadmin/Desktop/chromedriver', chrome_options=chrome_options)
driver.get('https://es.surveymonkey.com/r/3HRXW3P')
time.sleep(2)
nxt_btn = driver.find_element_by_name('NextButton')
nxt_btn.click()
time.sleep(2)
vote_check = driver.find_element_by_id('linput_740142485_10_8428776065_0')
vote_check.click()
time.sleep(2)
nxt_btn = driver.find_element_by_name('NextButton')
nxt_btn.click()
driver.quit()
