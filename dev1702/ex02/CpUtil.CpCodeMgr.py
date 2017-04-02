# CpCodeMgr 클래스에는 여러 메서드가 존재하는데 그 중 GetStockListByMarket 메서드는 시장 구분에 따라 주식 종목을 리스트 형태로 제공해줍니다. 해당 메서드를 호출하기 위해 먼저 win32com.client 모듈을 import하고 CpCodeMgr 클래스에 대한 객체를 생성합시다.


import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
codeList = instCpCodeMgr.GetStockListByMarket(1)

kospi = {}
for code in codeList:
    name = instCpCodeMgr.CodeToName(code)
    kospi[code] = name

f = open('..\\data\\kospi.csv', 'w')
for key, value in kospi.items():
    f.write("%s,%s\n" % (key, value))
f.close()

for i, code in enumerate(codeList):
    secondCode = instCpCodeMgr.GetStockSectionKind(code)
    name = instCpCodeMgr.CodeToName(code)
    print(i, code, secondCode, name)