import pandas as pd
from pandas import DataFrame
import pandas_datareader as pdr
import FinanceDataReader as fdr
from math import sqrt 
from datetime import datetime


start = datetime(2020,1,2)
end = datetime(2020,8,31)

list = ['^KS11'
, '005930'
, '000660'
, '005935'
, '035420'
, '207940'
, '005380'
, '012330'
, '068270'
, '051910'
, '005490'
, '028260'
, '055550'
, '051900'
, '105560'
, '017670'
, '015760'
, '034730'
, '000270'
, '006400'
, '018260'
, '032830'
, '096770'
, '035720'
, '033780'
, '003550'
, '090430'
, '036570'
, '066570'
, '000810'
, '086790'
, '010950'
, '009150'
, '009540'
, '316140'
, '010130'
, '251270'
, '011170'
, '030200'
, '002790'
, '024110'
, '021240'
, '035250'
, '032640'
, '034220'
, '018880'
, '267250'
, '086280'
, '006800'
, '078930'
, '000720'
, '010140'
, '029780'
, '271560'
, '004020'
, '088980'
, '161390'
, '004990'
, '071050'
, '023530'
, '028050'
, '008770'
, '097950'
, '005830'
, '005940'
, '012750'
, '139480'
, '000120'
, '036460'
, '128940'
, '241560'
, '016360'
, '047810'
, '011070'
, '081660'
, '000210'
, '003670'
, '007070'
, '009830'
, '042660'
, '282330'
, '004170'
, '005387'
, '003410'
, '001040'
, '030000'
, '003490'
, '008930'
]

data = DataFrame(columns=['code', 'stdv', 'unreal', 'sharp'])
k = 0
for code in list:

# 코스피에 상장 '종목코드.KS'로 처리
    if code == '^KS11': 
        code = code 
    else: code = code + '.KS'
# get_data_yahoo API를 통해서 yahho finance의 주식 종목 데이터
    stock = pdr.get_data_yahoo(code, start, end)
    stock = stock.loc[:, ['Close']]
    ret = ((stock.loc['2020-08-31','Close'] - stock.loc['2020-01-02','Close'])/stock.loc['2020-01-02','Close'])*12/8
    stock['Change'] = 0
    for i in range(1, 166):
       stock['Change'].iloc[i] = (stock['Close'].iloc[i] - stock['Close'].iloc[i-1]) /stock['Close'].iloc[i-1]
    
    rf = 0.005
    stdv = stock['Change'].std()*sqrt(12)/sqrt(8)
    sharp = (ret * 12/8 - 0.005) / stdv  
    raw_data = {'code':code, 'stdv':stdv, 'unreal':ret, 'sharp':sharp}
    data = data.append(raw_data, ignore_index=True)

#print(data)
data.to_excel('sharp_v2.xlsx')

    



