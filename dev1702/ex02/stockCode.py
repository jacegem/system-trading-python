import win32com.client
inStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
for i in range(0,10):
    print(inStockCode.GetData(1,i))