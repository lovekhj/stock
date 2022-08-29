# from selenium.webdriver.common.by import By
#
# driver.find_element(By.XPATH, '//button[text()="Some text"]')
# driver.find_element(By.XPATH, '//button')
# driver.find_element(By.ID, 'loginForm')
# driver.find_element(By.LINK_TEXT, 'Continue')
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
# driver.find_element(By.NAME, 'username')
# driver.find_element(By.TAG_NAME, 'h1')
# driver.find_element(By.CLASS_NAME, 'content')
# driver.find_element(By.CSS_SELECTOR, 'p.content')
#
# driver.find_elements(By.ID, 'loginForm')
# driver.find_elements(By.CLASS_NAME, 'content')


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
# xattr -d com.apple.quarantine chromedriver

browser = webdriver.Chrome(executable_path='/opt/homebrew/bin/chromedriver')
browser.maximize_window()



