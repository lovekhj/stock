import requests
from bs4 import BeautifulSoup
import lxml
import interestItem as iITEM


# print(iITEM.interstItemList)

# 삼성전자
url = 'https://finance.naver.com/item/main.naver?code=005930'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
res = requests.get(url, headers=headers)

# 주식종목, 현재주가, 전일가, 전일대비 금액, 상승/하락%
soup = BeautifulSoup(res.text, 'lxml')
stock_price = soup.find('div', attrs={'class','today'}).find('span','blind')
stock_price_yesterday = soup.find('div', attrs={'class','today'})
# print(stock_price_yesterday)
