# https://data-rider.blogspot.kr/2016/01/api_16.html
# 맥에서는 jupyter 로 접속한다


'''
References
COM (Component Object Model)
마이크로소프트가 개발한 소프트웨어 구성 요소들의 응용 프로그램 이진 인터페이스이다.

본문 참고 사이트
https://wikidocs.net/2870

웹 API 가이드
http://cybosplus.github.io
'''



import win32com.client
cursor = win32com.client.Dispatch("CpUtil.CpStockCode")
MAX = curosr.GetCount()
code_map = []
for i in range(MAX):
    code_map.append((cursor.GetData(0,i),
                     cursor.GetData(1,i),
                     cursor.GetData(2,i)))
df = pd.DataFrame(code_map,columns=['code','name','full_code'])
df = df[ df['code'].apply(lambda i: i[0] == 'A') ]
df.to_sql(name='item_names',con=conn,index=True,if_exists='replace')

# 종목에 대한 분단위 기간 데이터 추출 하기
def insert_item(code,start_date,end_date):
    cursor = win32com.client.Dispatch("CpSysDib.StockChart")
    cursor.SetInputValue(0, code)  # 코드 이름으로 종목 선택
    cursor.SetInputValue(1, ord("1")) # 기간 단위로 받기
    cursor.SetInputValue(2, end_date)  # 날짜 이하
    cursor.SetInputValue(3, start_date)  # 날짜 이상
    cursor.SetInputValue(5, (0, 1, 2, 8)) # 날짜, 시간, 시가, 거래량
    cursor.SetInputValue(6, ord("m"))  # 분단위 추출

    cursor.BlockRequest()   # 서버에 데이터 요청

    _rows = cursor.GetHeaderValue(3)  # 데이터 갯수
    _cols = cursor.GetHeaderValue(1)  # 추출 필드 갯수 setInputValue(5,x) 항목

    _df = pd.DataFrame()
    # GetDataValue
    for i in range(_rows):
        _rec = [];
        for j in range(_cols):
            rec.append(cursor.GetDataValue(j, i))
        _df = _df.append([_rec])
    _df.columns = ('date','time','price','volume')
    _df.to_sql(name="item_"+code,con=conn,index=False,if_exists='append')