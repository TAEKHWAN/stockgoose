# 네이버에서 주식정보를 가져오기
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
sys.path.append('C:/Users/admin/Desktop/IDT')
import IDT

class web_crawler():
    def __init__(self):
        self.naver_finance()

    def naver_finance(self):
        #최대 페이지 수 구하기 
        url="https://finance.naver.com/sise/sise_market_sum.nhn?&page=2"
        # google User Agent 검색해서 나의 User Agent 값을 찾은 다음 
        res = requests.get(url, headers=IDT.headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        pagelist = soup.find("table",attrs={"class":"Nnavi"}).find("td", attrs={"class":"pgRR"}).a["href"]
        maxpage = int(str(pagelist[pagelist.find("=")+1:100]))

        #모든 페이지에 대한 주식 정보 모으기
        for pages in range(1,maxpage):
            url="https://finance.naver.com/sise/sise_market_sum.nhn?&page={}".format(str(pages))
            data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
            data= []
            for row in data_rows:
                columns = row.find_all("td")
                if len(columns)<= 1: 
                    continue
                for column in columns: 
                    col_data = column.get_text().strip()
                    data.append(col_data)
                print(data)
                data.clear()
                
if __name__ == "__main__":
    print("__main__: 데이터수집")
    web_crawler = web_crawler()
