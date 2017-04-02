
import requests
import json
from bs4 import BeautifulSoup

url = 'http://www.krx.co.kr/por_kor/popup/JHPKOR13008.jsp'
r = requests.post(url, data={'mkt_typ':'S', 'market_gubun':'allVal'})

# print(r)


import requests

def get_sector(code):
    url = 'http://finance.naver.com/item/main.nhn?code='+code
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    sector = ""
    h4 = soup.find('h4', {'class':'h_sub sub_tit7'})
    if h4 is not None:
        sector = h4.a.text
    return sector

print(get_sector('005930'))