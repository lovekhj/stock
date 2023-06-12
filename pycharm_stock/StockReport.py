# 1. krx
#   (1) 전종목기본정보 (12005) - 파일다운로드
#   (2) 전종목지정내역 (12006) - 파일다운로드
#   (3) 위 파일 합치기
# 2. 네이버
#   (1) 시가총액 - 코스피/코스닥
#   (2) 업종별시세 - 전체리스트
#               - 상세리스트
#   (3) 테마별시세 - 주도주
#               - 상세리스트
#   (4) 상한가종목
#   (5) 급등종목
#   (6) 거래상위 - 거래량 1처만주이상 ( +종목만)
#

# import os.path
# import datetime
import os.path
import time
from datetime import datetime
from io import BytesIO

import bs4
import openpyxl
import requests
import pandas as pd
from bs4 import BeautifulSoup
import lxml


# golobal variable
global setHeader, gen_otp_url, down_url
global workDay, pathNm
global file_nm_1, file_nm_2, file_nm_3, file_nm_4
global upjongTitle, upjongLists

setHeader = ''
gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
down_url = f"http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd"
workDay = ''
pathNm = ''
file_nm_1 = ''
file_nm_2 = ''
file_nm_3 = ''
file_nm_4 = ''


upjongTitle = []
upjongLists = []



# 참고
# :%s/today/workDay/g



# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# KRX START
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# ----------------------------------------------------------------------------
# krx 정보실행
# ----------------------------------------------------------------------------
def krx_exec():
    # otp url
    otpUrl1 = "dbms/MDC/STAT/standard/MDCSTAT01901"
    otpUrl2 = "dbms/MDC/STAT/standard/MDCSTAT02001"

    # # krx 전종목기본정보 가져오기
    # krx_12005("krx_12005(전종목기본정보)", file_nm_1, otpUrl1)
    #
    # # krx 전종목지정내역
    # krx_12006("krx_12006(전전종목지정내역)", file_nm_2, otpUrl2)


# ----------------------------------------------------------------------------
# krx_12005(전종목기본정보 - 파일다운로드)
# ----------------------------------------------------------------------------
def krx_12005(title, file_nm, otpUrl):
    getPrintLine(80, title, "start")

    # otp down load
    resContent = getOtpCode(otpUrl)
    # 파일다운로드
    filedownload({ "code": resContent}, file_nm)

    getPrintLine(80, "krx_12005(전종목기본정보)", "end")

# ----------------------------------------------------------------------------
# krx_12006(전종목지정내역 - 파일다운로드)
# ----------------------------------------------------------------------------
def krx_12006(title, file_nm, otpUrl):
    getPrintLine(80, title, "start")

    # otp download
    resContent = getOtpCode(otpUrl)
    # 파일다운로드
    filedownload({ "code": resContent}, file_nm)

    getPrintLine(80, title, "end")




# ----------------------------------------------------------------------------
# otp code 가져오기
# ----------------------------------------------------------------------------
def getOtpCode(otpUrl):
    query_str_params = getQueryStrParams(otpUrl)
    res = requests.get(gen_otp_url, query_str_params, headers=setHeader)
    time.sleep(1.0)
    res.raise_for_status()
    return res.content

# ----------------------------------------------------------------------------
# query string
# ----------------------------------------------------------------------------
def getQueryStrParams(otpUrl):
    query_str_params = {
        "locale": "ko_KR",
        "mktId": "ALL",
        "share": "1",
        "csvxls_isNo": "false",
        "name": "fileDown",
        "url": otpUrl
    }
    return query_str_params

# ----------------------------------------------------------------------------
# krx 파일 다운로드
# ----------------------------------------------------------------------------
def filedownload(code, file_nm):
    down_csv = requests.post(down_url, code, headers=setHeader)
    time.sleep(2.0)
    down_csv.raise_for_status()
    # file은 바이너리스림으로 넘어온다. 처리는  BytesIO로 처리
    df = pd.read_csv(BytesIO(down_csv.content), encoding='EUC-KR')
    df.to_excel(pathNm+"/"+file_nm)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# KRX END
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# NAVER START
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# ----------------------------------------------------------------------------
# naver 정보실행
# ----------------------------------------------------------------------------
def naver_exec():

    # krx_12005("krx_12005(전종목기본정보)", file_nm_1, otpUrl1)
    # naver 업종
    naver_upjong("Naver업종")
    naver_upjong_list("Naver업종 리스트")

    # naver 테마
    # naver 시가총액
    # naver 배당금

# ----------------------------------------------------------------------------
# naver_upjong_list(네이버업종 리스트)
# ----------------------------------------------------------------------------
def naver_upjong_list(title):
    getPrintLine(80, title, "start")
    defaultUrl = "https://finance.naver.com/"
    url = "https://finance.naver.com/sise/sise_group.naver?type=upjong"

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    upjonglistsAll = soup.find('table', attrs={'class': 'type_1'}).find_all('tr')
    for upjonglists in upjonglistsAll:
        upjonglist = upjonglists.find_all('td')
        # print(upjonglist)
        if (len(upjonglist) > 1):
            for upjong in upjonglist[0:1]:
                upjongNm = upjonglist[0].get_text().strip()
                upjongValue = upjonglist[1].get_text().strip()
                print(upjongNm, upjongValue)
                upjongTitle.append({'upjongNm': upjongNm, 'upjongValue':upjongValue})

    # excel file 저장
    df1 = pd.DataFrame(upjongTitle)
    df1.to_excel(pathNm+'/'+file_nm_4)

    getPrintLine(80, title, "end")


# ----------------------------------------------------------------------------
# naver_upjong(네이버업종-상세)
# ----------------------------------------------------------------------------
def naver_upjongDetail(detailUrl, upjongNm):
    # print(detailUrl, upjongNm)
    res = requests.get(detailUrl)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    detailUpjongs = soup.find('table', attrs={'class':'type_5'}).find_all('div', attrs={'class':'name_area'})
    for idx, stockNm in enumerate(detailUpjongs):
        stockId = stockNm.find('a')['href'].split('=')[1]
        stockNm = stockNm.find('a').get_text().strip()
        upjongLists.append({'stockId':stockId, 'stockNm': stockNm, 'upjongNm':upjongNm})

# ----------------------------------------------------------------------------
# naver_upjong(네이버업종)
# ----------------------------------------------------------------------------
def naver_upjong(title):
    getPrintLine(80, title, "start")
    defaultUrl = "https://finance.naver.com/"
    url = "https://finance.naver.com/sise/sise_group.naver?type=upjong"

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    listsUpjong = soup.find('table', attrs={'class':'type_1'}).find_all('a')
    # for idx, listUpjong in enumerate(listsUpjong[0:1]):
    for idx, listUpjong in enumerate(listsUpjong):
        upjongDetailUrl = defaultUrl + listUpjong['href']
        upjongNm = listUpjong.get_text().strip()
        # print(idx, upjongDetailUrl, listUpjong.get_text().strip())
        naver_upjongDetail(upjongDetailUrl, upjongNm)

    # excel file 저장
    df1 = pd.DataFrame(upjongLists)
    df1.to_excel(pathNm+'/'+file_nm_3)

    getPrintLine(80, title, "end")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# NAVER END
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# ----------------------------------------------------------------------------
# print처리
# ----------------------------------------------------------------------------
def getPrintLine(count, job, gubun):
    jobTime = datetime.today().strftime("%Y:%m:%d %H-%M-%S")
    print("*"*count)
    print(" {} : {}: {}".format(job, gubun, jobTime))
    print("*"*count)

# ----------------------------------------------------------------------------
# 헤더 지정하기
# ----------------------------------------------------------------------------
def setHeaderKrx():
    setHeader = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Referer": "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020202"
    }




# ----------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    title = "주식기본정보 가져오기"
    getPrintLine(100, title, "start")

    # 기본변수
    setHeaderKrx()

    workDay = datetime.today().strftime("%Y%m%d")

    pathNm = './StockReportDb/' + workDay
    if not os.path.isdir(pathNm): os.mkdir(pathNm)


    # file nm
    file_nm_1 = "01_krx_stock_basic_"+workDay +'.xlsx' # 01_krx_stock_basic_20230610.xlsx
    file_nm_2 = "02_krx_stock_jijung_"+workDay +'.xlsx' # 02_krx_stock_jijung_20230610.xlsx
    file_nm_3 = "03_naver_stock_upjong_"+workDay +'.xlsx' # 02_krx_stock_jijung_20230610.xlsx
    file_nm_4 = "03_naver_stock_upjongTitle_"+workDay +'.xlsx' # 02_krx_stock_jijung_20230610.xlsx

    print("-" * 80)
    print("작업일자 ==> ", workDay)
    print("전종목기본정보      : file_nm_1 ==> {}".format(file_nm_1))
    print("전종목지정내역      : file_nm_2 ==> {}".format(file_nm_2))
    print("업종             : file_nm_3 ==> {}".format(file_nm_3))
    print("업종Title        : file_nm_4 ==> {}".format(file_nm_4))
    print("-" * 80)

    # krx 실행
    # ----------------------------
    krx_exec()
    # ----------------------------

    # Naver 실행
    # ----------------------------
    naver_exec()
    # ----------------------------



    getPrintLine(100, title, "end")
