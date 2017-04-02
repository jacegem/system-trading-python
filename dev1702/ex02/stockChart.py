import win32com.client
inStockChart = win32com.client.Dispatch("CpSysdib.StockChart")
inStockChart.SetInputValue(0, "A003540")        # 대신증권 코드
inStockChart.SetInputValue(1, '2')
inStockChart.SetInputValue(4, 60)
inStockChart.SetInputValue(5, 8)
inStockChart.SetInputValue(6, ord('D'))
inStockChart.SetInputValue(9, '1')
inStockChart.BlockRequest()
num = inStockChart.GetHeaderValue(3)
print(num)

data = []
for i in range(num):  # 60개의 데이터에 대해서 for 문을 돌린다.
    volumn = inStockChart.GetDataValue(0, i)  # 0번 부터 59번까지 데이터를 하나씩 가져온다. (거래량)
    data.append(volumn)

print (data)

