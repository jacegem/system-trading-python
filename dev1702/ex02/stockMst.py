import win32com.client
inStockMst = win32com.client.Dispatch("dscbo1.StockMst")
inStockMst.SetInputValue(0, "A000660")   # 삼성전자 주식이라는 정보를 입력
inStockMst.BlockRequest()       # 소스코드를 작성하는 경우에는 Request() 대신 BlockRequest()를 이용하면 됩니다
value = inStockMst.GetInputValue(0)             # 요청 된 데이터 중 삼성전자 주식의 가격정보를 얻어오는 부분
print(value)