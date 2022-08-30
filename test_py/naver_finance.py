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
import os

# xattr -d com.apple.quarantine chromedriver

# windows
# browser = webdriver.Chrome()

# mac
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

# browser.maximize_window()

# 1. page  dlehd
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)

# 2. 조회항목 초기화 (해제)
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected(): # 체크된상태
        checkbox.click() # 체크해제

# 3. 조회항목 설정
items_to_select = ['영업이익', '자산총계', '매출액']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..')  # 부모 엘리먼트를 찾음 -> td
    label = parent.find_element(By.TAG_NAME, 'label')
    # print(label.text)
    if label.text in items_to_select: # 선택항목과 일치 하면 선택한다
        checkbox.click() # check 한다.

# 4. 적용하기 버튼 클릭
# btn_apply = browser.find_element(By.XPATH, '//*[@id="contentarea_left"]/div[2]/form/div/div/div/a[1]')
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]') # // :전체에서 찾는다.
btn_apply.click()

for idx in range(1, 40): # 1이상 40미만 페이지 반복
    # 사전작업 : 페이지 이동
    browser.get(url + str(idx))
    # 5. 데이터 추출
    df = pd.read_html(browser.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True) # 줄 전체가 빈공간이면 지운다. row단위
    df.dropna(axis='columns', how='all', inplace=True) # 칼럼기준 삭제

    # 페이지 데이터 없을 경우 나옴
    if len(df) == 0:
        break

    # 6. 파일저장
    f_name = 'sise.csv'
    if os.path.exists(f_name): # 파일이 있다면, header제외
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
    else:
        df.to_csv(f_name, encoding='utf-8-sig', index=False)
    print(f'{idx} 페이지 완료')

browser.quit() # 페이지 종료







