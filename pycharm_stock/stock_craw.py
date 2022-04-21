import requests
from bs4 import BeautifulSoup
import re
import time
from io import BytesIO
import pandas as pd
import datetime
import glob
import os




global upjong_lists
upjong_lists = []
global theme_lists
theme_lists = []

url_basic = 'https://finance.naver.com'

# 전종목기본정보
def krx_stock_basic(dt_str):
    # 전종목기본정보 : 파일명만들기
    file_nm = '전종목기본정보_' + dt_str + '.xlsx'

    # otp 데이터 가져오기
    gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
        "Refer": "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020103"}
    query_str_params = {
        "locale": "ko_KR",
        "mktId": "ALL",
        "share": "1",
        "csvxls_isNo": "false",
        "name": "fileDown",
        "url": "dbms/MDC/STAT/standard/MDCSTAT01901"
    }

    res = requests.get(gen_otp_url, query_str_params, headers=headers)
    time.sleep(1.0)  # 1초
    res.raise_for_status()
    code = {
        "code": res.content
    }

    # 파일다운로드
    # download.cmd 에서 General의 Request URL 부분
    down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
    # requests Module의 post함수를 이용하여 해당 url에 접속하여 otp코드를 제출함

    down_csv = requests.post(down_url, code, headers=headers)
    time.sleep(1.0)
    # 다운 받은 csv파일을 pandas의 read_csv 함수를 이용하여 읽어 들임.
    # read_csv 함수의 argument에 적합할 수 있도록 BytesIO함수를 이용하여 바이너 스트림 형태로
    df = pd.read_csv(BytesIO(down_csv.content), encoding='EUC-KR')
    df.to_excel(folder_nm + '/' + file_nm)
    print('download complate ==> {}'.format(file_nm))


# 전종목지정내역
def krx_stock_jijung(dt_str):
    # 전종목지정내역 : 파일명만들기

    file_nm = '전종목지정내역_' + dt_str + '.xlsx'

    # otp 데이터 가져오기
    gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
        "Refer": "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020103"}
    query_str_params = {
        "locale": "ko_KR",
        "mktId": "ALL",
        "csvxls_isNo": "false",
        "name": "fileDown",
        "url": "dbms/MDC/STAT/standard/MDCSTAT02001"
    }

    res = requests.get(gen_otp_url, query_str_params, headers=headers)
    time.sleep(1.0)  # 1초
    res.raise_for_status()
    code = {
        "code": res.content
    }

    # 파일다운로드
    # download.cmd 에서 General의 Request URL 부분
    down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
    # requests Module의 post함수를 이용하여 해당 url에 접속하여 otp코드를 제출함

    down_csv = requests.post(down_url, code, headers=headers)
    time.sleep(1.0)
    # 다운 받은 csv파일을 pandas의 read_csv 함수를 이용하여 읽어 들임.
    # read_csv 함수의 argument에 적합할 수 있도록 BytesIO함수를 이용하여 바이너 스트림 형태로
    df = pd.read_csv(BytesIO(down_csv.content), encoding='EUC-KR')
    df.to_excel(folder_nm + '/' + file_nm)
    print('download complate ==> {}'.format(file_nm))


# PER/PBR/배당수익률(개별종목)
def krx_stock_per_pbr(dt_str):
    # PER/PBR/배당수익률(개별종목) : 파일명만들기
    # dt_str = '20220318'
    file_nm = 'per_pbr_배당_' + dt_str + '.xlsx'

    # otp 데이터 가져오기
    gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
        "Refer": "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020103"}
    query_str_params = {
        "locale": "ko_KR",
        "searchType": "1",
        "mktId": "ALL",
        "trdDd": dt_str,
        "csvxls_isNo": "false",
        "name": "fileDown",
        "url": "dbms/MDC/STAT/standard/MDCSTAT03501"
    }

    print(query_str_params)

    res = requests.get(gen_otp_url, query_str_params, headers=headers)
    time.sleep(1.0)  # 1초
    res.raise_for_status()
    code = {
        "code": res.content
    }

    # 파일다운로드
    # download.cmd 에서 General의 Request URL 부분
    down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
    # requests Module의 post함수를 이용하여 해당 url에 접속하여 otp코드를 제출함

    down_csv = requests.post(down_url, code, headers=headers)
    time.sleep(2.0)
    # 다운 받은 csv파일을 pandas의 read_csv 함수를 이용하여 읽어 들임.
    # read_csv 함수의 argument에 적합할 수 있도록 BytesIO함수를 이용하여 바이너 스트림 형태로
    df = pd.read_csv(BytesIO(down_csv.content), encoding='EUC-KR')
    # df
    df.to_excel(folder_nm + '/' + file_nm)
    print('download complate ==> {}'.format(file_nm))


# 전종목시세 (전종목시세 [12001])
def krx_stock_sise(dt_str):
    # 전종목시세_ : 파일명만들기  --> 화면크롤링 해야 함.

    file_nm = '전종목시세_' + dt_str + '.xlsx'

    # otp 데이터 가져오기
    gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
        "Refer": "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020103"}
    query_str_params = {
        "locale": "ko_KR",
        "mktId": "ALL",
        "trdDd": dt_str,
        "share": "1",
        "money": "1",
        "csvxls_isNo": "false",
        "name": "fileDown",
        "url": "dbms/MDC/STAT/standard/MDCSTAT01501"
    }

    res = requests.get(gen_otp_url, query_str_params, headers=headers)
    time.sleep(1.0)  # 1초
    res.raise_for_status()
    code = {
        "code": res.content
    }

    # 파일다운로드
    # download.cmd 에서 General의 Request URL 부분
    down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
    # requests Module의 post함수를 이용하여 해당 url에 접속하여 otp코드를 제출함

    down_csv = requests.post(down_url, code, headers=headers)
    time.sleep(1.0)
    # 다운 받은 csv파일을 pandas의 read_csv 함수를 이용하여 읽어 들임.
    # read_csv 함수의 argument에 적합할 수 있도록 BytesIO함수를 이용하여 바이너 스트림 형태로

    df = pd.read_csv(BytesIO(down_csv.content), encoding='EUC-KR')
    df.to_excel(folder_nm + '/' + file_nm)
    print('download complate ==> {}'.format(file_nm))



# ################################################################################
# 프로그램시작
# ################################################################################
#  기초정보
# --------------------------------------------------------------------------------
# 0은 월요일, 1은 화요일, 2는 수요일, 3은 목요일, 4는 금요일 ,5는 토요일 ,6은 일요일
weekday_str = datetime.datetime.now().weekday() # 주 :일자로 변환
if weekday_str == 6 :
    dt_time = datetime.datetime.now() - datetime.timedelta(days=2)
elif weekday_str == 5 :
    dt_time = datetime.datetime.now() - datetime.timedelta(days=1)
else:
    dt_time = datetime.datetime.now()

dt_str = datetime.datetime.strftime(dt_time, '%Y%m%d')
print('작업일자 ==> ', dt_str)

# 폴더 - 변경(stock_docu/yyyymmdd)
# --------------------------------------------------------------------------------
folder_nm = '주식_' + dt_str
path = './' + folder_nm
if os.path.isdir(path) == False : os.mkdir(folder_nm)


# --------------------------------------------------------------------------------
# 함수호출
# --------------------------------------------------------------------------------

# 전종목기본정보 (전종목기본정보 [12005])
# krx_stock_basic(dt_str)

# 전종목지정내역(전종목지정내역[12006])
# krx_stock_jijung(dt_str)

# PER/PBR/배당수익률(개별종목)(PER/PBR/배당수익률(개별종목) [12021])
# krx_stock_per_pbr(dt_str)

# 전종목시세 (전종목시세 [12001])
# krx_stock_sise(dt_str)

# (기준정보)업종별 시세


# (기준정보)테마