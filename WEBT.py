# 네이버에서 주식정보를 가져오기
import stockgoose.IDT
import requests
from bs4 import BeautifulSoup

url= "https://kr.investing.com/stock-screener/?sp=country::11|sector::a|industry::a|equityType::a%3Ceq_market_cap;"
# google User Agent 검색해서 나의 User Agent 값을 찾은 다음 
res = requests.get(url, headers=IDT.headers)
res.raise_for_status()
print(res)