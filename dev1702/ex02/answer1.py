import win32com.client
inStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
numStocks = inStockCode.GetCount()
for i in range(0, numStocks):
    if "NAVER" in inStockCode.GetData(1,i):
        print(i, inStockCode.GetData(1,i))
