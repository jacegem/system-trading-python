import win32com.client
inCpSvr7223 = win32com.client.Dispatch("dscbo1.CpSvr7223")

inCpSvr7223.SetInputValue(0, ord('4'))                # 일자별
inCpSvr7223.SetInputValue(1, '001')

inCpSvr7223.BlockRequest()

num = inCpSvr7223.GetHeaderValue(1)

for x in range(num):
    print( inCpSvr7223.GetDataValue(0,x))


