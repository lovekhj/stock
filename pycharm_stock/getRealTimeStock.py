import requests
from bs4 import BeautifulSoup
import lxml
import interestItem as iITEM
import telegramBot as tb
import time


# 실시간 증권검색

def get_stock_realTime(stock_id, stock_nm):
    url = 'https://finance.naver.com/item/main.naver?code={}'.format(stock_id)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
    res = requests.get(url, headers=headers)

    # 주식종목, 현재주가, 전일가, 전일대비 금액, 상승/하락%
    soup = BeautifulSoup(res.text, 'lxml')
    stock_price = soup.find('div', attrs={'class','today'}).find('span','blind').text
    stock_price_yesterday = soup.find('div',attrs={'class','rate_info'}).find('td', attrs={'class','first'}).find('span','blind').text
    stock_price_chai = soup.find('p','no_exday').find('span','blind').text
    stock_price_chai_rate = soup.find('p','no_exday').find_all('span', attrs={'class','blind'})[1].text +\
                            soup.find('p','no_exday').find('span', attrs={'class','per'}).text

    try:
        stock_price_chai_1 = soup.find('p','no_exday').find_all('span', attrs={'class', 'ico'})[0].text
    except:
        stock_price_chai_1 = ""

    try:
        stock_price_chai_2 = soup.find('p','no_exday').find_all('span', attrs={'class', 'ico'})[1].text
    except:
        stock_price_chai_2 = ""

    # print(stock_price_chai)

    stock_all = "{}({}) 현재가({}) 전일가({}) 차이({} {}원)({}{})".format(stock_id, stock_nm, stock_price
                                                                  , stock_price_yesterday
                                                                  , stock_price_chai_1, stock_price_chai
                                                                  , stock_price_chai_2, stock_price_chai_rate)
    print(stock_all)
    tb.send_telegram_bot(stock_all)
    time.sleep(1)

stockLists = iITEM.interstItemList
for idx, stockList in enumerate(stockLists):
    stock_id = stockList.split(',')[0]
    stock_nm = stockList.split(',')[1]
    # printnt(idx, stock_id, stock_nm)
    get_stock_realTime(stock_id, stock_nm)

# url = 'https://finance.naver.com/item/main.naver?code=005930'
# url = 'https://finance.naver.com/item/main.naver?code=000660'
# get_stock_realTime('005930', '삼성전자')
# get_stock_realTime('000660', 'SK하이닉스')
# get_stock_realTime('001500', '현대차증권')




