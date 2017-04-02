
import win32com.client
import re

class StockCodes:

    def savecodes(self):
        instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
        codeList = instCpCodeMgr.GetStockListByMarket(1)

        kospi = {}
        for code in codeList:
            name = instCpCodeMgr.CodeToName(code)
            kospi[code] = name

        f = open('..\\data\\kospi.csv', 'w')
        for key, value in kospi.items():
            if self.is_unable_read_code(key, value) == True: continue
            f.write("%s,%s\n" % (key, value))
        f.close()

    def is_unable_read_code(self, code, name):
        pattern = r'^KOSPI|KODEX|SMART|ARIRANG|KBSTAR|TIGER|KINDEX|KOSEF|대신B\d{3}'
        if re.match(pattern, name): return True
        if re.match(r'\d+호$', name): return True
        if re.match(r'^Q', code): return True
        return None

if __name__ == "__main__":
    stockcode = StockCodes()
    stockcode.savecodes()





# Regex regex = new Regex(@"KOSPI|KODEX|SMART|ARIRANG|KBSTAR|TIGER|KINDEX|KOSEF|대신B\d{3}");
