# 네이버에서 주식정보를 가져오기
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import sys
sys.path.append('C:/Users/admin/Desktop/IDT')
import IDT

for pages in range(1,53):
    
    url= "https://kr.investing.com/stock-screener/?sp=country::11|sector::a|industry::a|equityType::a%3Ceq_market_cap;{}".format(pages)
    # google User Agent 검색해서 나의 User Agent 값을 찾은 다음 
    res = requests.get(url, headers=IDT.headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")


    title = "종목 기호 거래소 종가 변동 시가총액 거래량 "