import requests
from bs4 import BeautifulSoup
import lxml
import interestItem as iITEM
import telegramBot as tb


# print(iITEM.interstItemList)

stock_id = '005930'
stock_nm = '삼성전자'


# 삼성전자
url = 'https://finance.naver.com/item/main.naver?code={}'.format(stock_id)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
res = requests.get(url, headers=headers)

# 주식종목, 현재주가, 전일가, 전일대비 금액, 상승/하락%
soup = BeautifulSoup(res.text, 'lxml')
stock_price = soup.find('div', attrs={'class','today'}).find('span','blind').text
stock_price_yesterday = soup.find('div',attrs={'class','rate_info'}).find('td', attrs={'class','first'}).find('span','blind').text
stock_price_chai = soup.find('div', attrs={'class','today'}).find_all('em',attrs={'class','no_down'})[1].find('span','blind').text
stock_price_chai_rate = soup.find('div', attrs={'class','today'}).find_all('em',attrs={'class','no_down'})[2].find('span','blind').text +\
                        soup.find('div', attrs={'class','today'}).find_all('em',attrs={'class','no_down'})[2].find('span','per').text

stock_all = "주식종목 : {}:{} 현재가:{}, 전일가:{}, 전일대비:{}({})".format(stock_id, stock_nm, stock_price \
                                                              , stock_price_yesterday
                                                              , stock_price_chai
                                                              , stock_price_chai_rate)
print(stock_all )
tb.send_telegram_bot(stock_all)

