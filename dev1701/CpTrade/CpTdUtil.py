'''
CpTdUtil
설명 : 주문 오브젝트를 사용하기 위해 필요한 초기화 과정들을 수행한다
 모든 주문오브젝트는 사용하기 전에, 필수적으로 TradeInit을 호출한 후에 사용할 수 있다.
 전역변수(글로벌 변수) 로 선언하여 사용하여야 합니다.
'''

import win32com.client
cpTdUtil = win32com.client.Dispatch("CpTrade.CpTdUtil")

# 주문 초기화
# 초기화 에러 발생시 메시지 출력
ret = cpTdUtil.TradeInit(0)

accountNumber = cpTdUtil.AccountNumber

print(accountNumber)
# ('335261524',)


# http://iamaman.tistory.com/1387
# ahk 자동실행






