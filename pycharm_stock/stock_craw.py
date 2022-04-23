import requests
from bs4 import BeautifulSoup
import re
import time
from io import BytesIO
import pandas as pd
import datetime
import glob
import os
import json
import lxml
import pandas as pd

global path_nm, upjong_lists, theme_lists, siljuk_lists
global file_nm_1, file_nm_2, file_nm_3, file_nm_4, file_nm_5, file_nm_6, file_nm_result, file_siljuk_nm
path_nm = ''
upjong_lists = []
theme_lists = []
siljuk_lists = []

file_nm_1 = ''
file_nm_2 = ''
file_nm_3 = ''
file_nm_4 = ''
file_nm_5 = ''
file_nm_6 = ''
file_nm_result = ''
file_siljuk_nm = ''

url_basic = 'https://finance.naver.com'


# 전종목기본정보
def krx_stock_basic(dt_str):
    # 전종목기본정보 : 파일명만들기
    # file_nm = '전종목기본정보_' + dt_str + '.xlsx'
    # file_nm_1 = '01_krx_stoc_basic_' + dt_str + '.xlsx'

    print("*" * 80)
    print('전종목기본정보 ==> start')

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
    df.to_excel(path_nm + '/' + file_nm_1)

    print('전종목기본정보 ==> end  : {}'.format(file_nm_1))
    print("*" * 80)


# 전종목지정내역
def krx_stock_jijung(dt_str):
    # 전종목지정내역 : 파일명만들기
    # file_nm = '전종목지정내역_' + dt_str + '.xlsx'

    print("*" * 80)
    print('전종목지정내역 ==> start')

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
    df.to_excel(path_nm + '/' + file_nm_2)

    print('전종목지정내역 ==> end  : {}'.format(file_nm_2))
    print("*" * 80)


# PER/PBR/배당수익률(개별종목)
def krx_stock_per_pbr(dt_str):
    # PER/PBR/배당수익률(개별종목) : 파일명만들기
    # file_nm = 'per_pbr_배당_' + dt_str + '.xlsx'

    print("*" * 80)
    print('PER/PBR/배당수익률(개별종목) ==> start')

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

    # print(query_str_params)

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
    df.to_excel(path_nm + '/' + file_nm_3)

    print('PER/PBR/배당수익률(개별종목) ==>  end  : {}'.format(file_nm_3))
    print("*" * 80)


# 전종목시세 (전종목시세 [12001])
def krx_stock_sise(dt_str):
    # 전종목시세_ : 파일명만들기  --> 화면크롤링 해야 함.
    # file_nm = '전종목시세_' + dt_str + '.xlsx'

    print("*" * 80)
    print('전종목시세 ==> start')

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
    df.to_excel(path_nm + '/' + file_nm_4)

    print('전종목시세 ==>  end  : {}'.format(file_nm_4))
    print("*" * 80)


# upjong detail
def get_upjong_detail(idx, url, upjongNm):
    # print(idx, url, upjongNm)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    upjong_details = soup.find_all('div', attrs={'class': 'name_area'})
    for upjong_detail in upjong_details:
        code_nm = upjong_detail.find('a').get_text()
        code = upjong_detail.find('a')['href'].split('=')[1]
        # print(code, code_nm, upjongNm)
        upjong_lists.append({'종목코드': code, '종목명': code_nm, '업종': upjongNm})


# (기준정보)업종별 시세
def upjong_sise(dt_str):
    # file_nm = '업종상세_' + dt_str + '.xlsx'
    # file_json_temp = '업종상세.json'

    print("*" * 80)
    print('업종별 시세 ==> start')

    file_json_temp = 'upjong_detail.json'

    url = 'https://finance.naver.com/sise/sise_group.naver?type=upjong'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
    res = requests.get(url)
    res.raise_for_status()
    url_basic = 'https://finance.naver.com'
    soup = BeautifulSoup(res.text, 'lxml')
    upjongs = soup.find('table', attrs={'class': 'type_1'}).find_all('a')
    for idx, upjong in enumerate(upjongs):
        url = url_basic + upjong['href']
        upjongNm = upjong.get_text().strip()
        get_upjong_detail(idx, url, upjongNm)
        # time.sleep(1.0)

    with open(path_nm + '/' + file_json_temp, 'w') as outfile:
        json.dump(upjong_lists, outfile)

    print('upjong complate ==> {}'.format(file_json_temp))

    with open(path_nm + '/' + file_json_temp, 'r') as json_file:
        json_data = json.load(json_file)

    # print(json_data)
    df_upjong = pd.json_normalize(json_data)
    df_upjong.to_excel(path_nm + '/' + file_nm_5)

    print('업종별 시세 ==> end  : {}'.format(file_nm_5))
    print("*" * 80)


# 테마 detail
def get_theme_detail(idx, url, themeNm):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    theme_details = soup.find_all('div', attrs={'class': 'name_area'})

    for theme_detail in theme_details:
        code = theme_detail('a')[0]['href'].split('=')[1]
        code_nm = theme_detail.get_text().replace('*', '')
        theme_lists.append({'종목코드': code, '종목명': code_nm, '테마': themeNm})


# (기준정보)테마
def theme_sise(dt_str):
    # file_theme_nm = '테마_' + dt_str + '.xlsx'
    # file_json_theme_temp = '테마.json'

    print("*" * 80)
    print('테마 시세 ==> start')

    file_json_theme_temp = 'theme_detail.json'
    # 1~7 page
    for i in range(1, 8):
        url = 'https://finance.naver.com/sise/theme.naver?&page={}'.format(i)
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
        res = requests.get(url)
        res.raise_for_status()
        url_basic = 'https://finance.naver.com'
        soup = BeautifulSoup(res.text, 'lxml')
        themes = soup.find_all('td', attrs={'class': 'col_type1'})

        for idx, theme in enumerate(themes):
            url = url_basic + theme('a')[0]['href']
            themeNm = theme.get_text()
            get_theme_detail(idx, url, themeNm)
            # time.sleep(1.0)

    with open(path_nm + '/' + file_json_theme_temp, 'w') as outfile:
        json.dump(theme_lists, outfile)

    print('theme complate ==> {}'.format(file_json_theme_temp))

    with open(path_nm + '/' + file_json_theme_temp, 'r') as json_file:
        json_data = json.load(json_file)

    # print(json_data)
    df_theme = pd.json_normalize(json_data)
    df_theme.to_excel(path_nm + '/' + file_nm_6)

    print('테마 시세 ==> end  : {}'.format(file_nm_6))
    print("*" * 80)


# 파일합치기
def get_sum_file(dt_str):
    print("*" * 80)
    print('파일 합치기 ==> start')

    # 전종목기본정보_20220320.xlsx
    # file_nm_1 = '전종목기본정보_' + dt_str + '.xlsx'
    df1 = pd.read_excel(path_nm + '/' + file_nm_1, index_col=0)
    # 칼럼변경 (단축코드->종목코드)
    df1.rename(columns={"단축코드": "종목코드"}, inplace=True)
    # 칼럼삭제 (표준코드)
    df1.drop(['표준코드', '한글 종목명', '영문 종목명', '상장일'], axis='columns', inplace=True)  # 칼럼단위 삭제
    # index = 종목코드
    df1.set_index('종목코드', inplace=True)
    # print(df1.head(10))

    # 전종목지정내역_20220320.csv
    # file_nm_2 = '전종목지정내역_'+dt_str+'.csv'
    # df2 = pd.read_csv(file_nm_2, encoding='cp949')
    # file_nm_2 = '전종목지정내역_'+dt_str+'.xlsx'
    df2 = pd.read_excel(path_nm + '/' + file_nm_2)
    # 칼럼삭제 (표준코드)
    # df2.drop(['종목명','Unnamed: 0'], axis='columns', inplace=True) # 칼럼단위 삭제
    df2.drop(['종목명'], axis='columns', inplace=True)  # 칼럼단위 삭제
    # index = 종목코드
    df2.set_index('종목코드', inplace=True)
    # print(df2.head(10))

    # per_pbr_배당_20220320.csv
    # file_nm_3 = 'per_pbr_배당_'+dt_str+'.csv'
    # df3 = pd.read_csv(file_nm_3, encoding='cp949')
    # file_nm_3 = 'per_pbr_배당_'+dt_str+'.xlsx'
    df3 = pd.read_excel(path_nm + '/' + file_nm_3)
    # 칼럼삭제 (표준코드)
    # df3.drop(['종목명', 'Unnamed: 0'], axis='columns', inplace=True) # 칼럼단위 삭제
    df3.drop(['종목명'], axis='columns', inplace=True)  # 칼럼단위 삭제
    # index = 종목코드
    df3.set_index('종목코드', inplace=True)
    # print(df3.head(10))

    # 업종상세_20220321.xlsx
    # file_nm_5 = '업종상세_'+dt_str+'.xlsx'
    df4 = pd.read_excel(path_nm + '/' + file_nm_5, usecols="B,D")
    # df4 = pd.read_excel(file_nm_5 )
    # 칼럼변경 (단축코드->종목코드)
    # df4.rename(columns={"종목코드":"종목코드1"}, inplace=True)
    df4.T.drop_duplicates().T
    df4.reset_index(drop=True)
    # index = 종목코드
    df4.set_index('종목코드', inplace=True)
    # print(df4.head(10))

    # 테마_20220321.xlsx
    # file_nm_6 = '테마_'+dt_str+'.xlsx'
    df5 = pd.read_excel(path_nm + '/' + file_nm_6, usecols="B,C,D", dtype={'종목코드': str})

    # df5 = df5.groupby(['종목코드','종목명'])['테마'].apply(', '.join).reset_index()
    df5 = df5.groupby(['종목코드'])['테마'].apply(', '.join).reset_index()
    # index = 종목코드
    df5.set_index('종목코드', inplace=True)
    # print(df5.head())

    # 저장파일명
    result_df = pd.concat([df1, df2, df3, df4, df5], axis=1)  # axis=1 좌우로 이어 붙여보기
    result_df.drop(['Unnamed: 0'], axis='columns', inplace=True)  # 칼럼단위 삭제
    # 한글 종목약명이 null인 index 찾기
    df_del_idx = result_df[result_df['한글 종목약명'].isnull()].index
    # 한글 종목약명이 null인 데이터 삭제
    result_df = result_df.drop(df_del_idx)
    result_df.reset_index(drop=False, inplace=True)

    result_df['조회항목'] = result_df['종목코드'] + ' ' + result_df['한글 종목약명']
    # 엑셀저장
    result_df.to_excel(path_nm + '/' + file_nm_result, sheet_name='total', na_rep='')

    print('파일 합치기 ==> end  : {}'.format(file_nm_result))
    print("*" * 80)


# 실적상세 가져오기 - naver
def siljuk_def(code, code_nm):
    url = 'https://finance.naver.com/item/main.naver?code={}'.format(code)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    # 종목코드, 명
    # ---------------------------------------------------------------------
    #     code = '098120'
    #     code_nm = '마이크로컨텍솔'

    #     siljuk_lists.append(['---------------------------------------------------------------------'])
    #     siljuk_lists.append([code, code_nm])
    #     siljuk_lists.append(['---------------------------------------------------------------------'])

    #     # 시가총액
    #     # ---------------------------------------------------------------------
    #     sum_amt_list =[code, code_nm, '시가총액']
    #     sum_amt = soup.find('div', attrs={'class':'first'}).find('td').get_text().split()[0]\
    #              + ' (' + soup.find('div', attrs={'class':'first'}).find('td').get_text().split()[1]\
    #              + ')'

    #     sum_amt_list.append(sum_amt)
    #     siljuk_lists.append(sum_amt_list)

    #     # 투자의견
    #     # ---------------------------------------------------------------------
    #     # PER/EPS 정보
    #     # ---------------------------------------------------------------------
    #     sum_per_list = [code, code_nm,'PER/EPS 정보']
    #     try :
    #         sum_per = soup.find('table', attrs={'class':'per_table'}).find('em', attrs={'id':'_per'}).get_text()+' (배)'
    #     except:
    #         sum_per = 'N/A'

    #     sum_per_list.append(sum_per)
    #     siljuk_lists.append(sum_per_list)

    #     동종업종 PER
    #     ---------------------------------------------------------------------
    #     ---------------------------------------------------------------------
    #     ---------------------------------------------------------------------

    # title
    # ---------------------------------------------------------------------
    try:
        titles = soup.find_all('div', attrs={'class': 'sub_section'})[4].find('thead').find_all('tr')[1].find_all('th')
    except:
        return

    sub_title = []
    sub_title.append('종목코드')
    sub_title.append('종목한글명')
    sub_title.append('주요재무정보')
    for title in titles:
        sub_title.append(title.get_text().strip())

    # 재무정보 실적
    # ---------------------------------------------------------------------
    siljuk_lists.append(sub_title)
    siljuks = soup.find_all('div', attrs={'class': 'sub_section'})[4].find('tbody').find_all('tr')
    for idx, siljuk in enumerate(siljuks):
        title = siljuk.find('th').get_text()
        title_values = []
        title_values.append(code)
        title_values.append(code_nm)
        title_values.append(title)
        sub_siljuk = siljuk.find_all('td')
        for a_value in sub_siljuk:
            sub_value = a_value.get_text().strip()
            title_values.append(sub_value)

        siljuk_lists.append(title_values)
    # ---------------------------------------------------------------------
    # siljuk_lists.append(['---------------------------------------------------------------------'])


# 실적(재무제표 가져오기)
def get_siljuk(dt_str):
    # file_siljuk_nm = '실적_' + dt_str + '.csv'

    print("*" * 80)
    print('실적(재무제표 가져오기) ==> start')

    # 전종목기본정보_20220320.xlsx
    # file_nm_1 = '전종목기본정보_' + dt_str + '.xlsx'
    df1 = pd.read_excel(path_nm + '/' + file_nm_1, index_col=0, dtype={'단축코드': str})
    # 칼럼변경 (단축코드->종목코드)
    df1.rename(columns={"단축코드": "종목코드"}, inplace=True)
    # 칼럼삭제 (표준코드)
    df1.drop(['표준코드', '한글 종목명', '영문 종목명', '상장일'], axis='columns', inplace=True)  # 칼럼단위 삭제
    # for column_name, item in df1.iteritems():
    for index, row in df1.iterrows():
        code = row[0]
        code_nm = row[1]
        # print(index, row[0], row[1])
        siljuk_def(code, code_nm)

    print('siljuk sub complete')
    # for siljuk_list in siljuk_lists:
    #     print(siljuk_list)

    with open(path_nm + '/' + file_siljuk_nm, 'w', encoding='utf-8') as f:
        for siljuk_list in siljuk_lists:
            data_l = ''
            for idx, data in enumerate(siljuk_list):
                # print(data, end='|')
                data_l = data_l + '|' + data

            f.write(data_l + '\n')

    print('실적(재무제표 가져오기) ==> end  : {}'.format(file_siljuk_nm))
    print("*" * 80)


# ################################################################################
# 프로그램시작
# ################################################################################

print("################################################################################");
print("주식기본정보 가져오기")
print("################################################################################");

#  기초정보
# --------------------------------------------------------------------------------
# 0은 월요일, 1은 화요일, 2는 수요일, 3은 목요일, 4는 금요일 ,5는 토요일 ,6은 일요일
weekday_str = datetime.datetime.now().weekday()  # 주 :일자로 변환
if weekday_str == 6:
    dt_time = datetime.datetime.now() - datetime.timedelta(days=2)
elif weekday_str == 5:
    dt_time = datetime.datetime.now() - datetime.timedelta(days=1)
else:
    dt_time = datetime.datetime.now()

dt_str = datetime.datetime.strftime(dt_time, '%Y%m%d')

print("*" * 80)
print('작업일자 ==> ', dt_str)
print("*" * 80)

# 폴더 - 변경(stock_docu/yyyymmdd)
# --------------------------------------------------------------------------------
folder_nm = 'stock_' + dt_str
path_nm = '../../stock_docu/' + folder_nm
if not os.path.isdir(path_nm): os.mkdir(path_nm)

print("파일명")
print("*" * 80)
file_nm_1 = '01_krx_stoc_basic_' + dt_str + '.xlsx'
file_nm_2 = '02_krx_stock_jijung_' + dt_str + '.xlsx'
file_nm_3 = '03_krx_stock_per_pbr_' + dt_str + '.xlsx'
file_nm_4 = '04_krx_stock_sise_' + dt_str + '.xlsx'
file_nm_5 = '05_upjong_sise_' + dt_str + '.xlsx'
file_nm_6 = '06_theme_sise_' + dt_str + '.xlsx'
file_nm_result = '00_total_' + dt_str + '.xlsx'
file_siljuk_nm = '11_siljuk_nm_' + dt_str + '.csv'

print("전종목기본정보      : file_nm_1 ==> {}".format(file_nm_1))
print("전종목지정내역      : file_nm_2 ==> {}".format(file_nm_2))
print("PER/PBR/배당수익률  : file_nm_3 ==> {}".format(file_nm_3))
print("전종목시세          : file_nm_4 ==> {}".format(file_nm_4))
print("업종별 시세         : file_nm_5 ==> {}".format(file_nm_5))
print("테마   시세         : file_nm_6 ==> {}".format(file_nm_6))
print("최종파일            : file_nm_result ==> {}".format(file_nm_result))
print("실적파일            : file_siljuk_nm ==> {}".format(file_siljuk_nm))

print("*" * 80)

# --------------------------------------------------------------------------------
# 함수호출
# --------------------------------------------------------------------------------

print("start")
# 전종목기본정보 (전종목기본정보 [12005])
krx_stock_basic(dt_str)

# 전종목지정내역(전종목지정내역[12006])
krx_stock_jijung(dt_str)

# PER/PBR/배당수익률(개별종목)(PER/PBR/배당수익률(개별종목) [12021])
krx_stock_per_pbr(dt_str)

# 전종목시세 (전종목시세 [12001])
krx_stock_sise(dt_str)

# (기준정보)업종별 시세
upjong_sise(dt_str)

# (기준정보)테마
theme_sise(dt_str)

# 파일합치기
get_sum_file(dt_str)

# 실적(재무제표 가져오기) - 1달에 한번 실행 (매월 1일)
# get_siljuk(dt_str)

print("end")
