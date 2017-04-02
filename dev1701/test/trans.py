# -*- coding: utf8 -*-

from urllib.parse   import quote
from urllib.request import urlopen

#str = quote('한글')
#url = "http://www.naver.com?q=" + str
# url = "http://translate.google.co.kr/translate_a/t?client=t&ie=UTF-8&oe=UTF-8&sl=ja&tl=ko&text='" +  'aa'
#url = 'https://translate.google.co.kr/translate_a/single?client=t&sl=ko&tl=en&hl=ko&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=btn&ssel=3&tsel=3&kc=0&tk=428279.55456&q=%ED%95%98%EC%9D%B4'
#response = urllib.request.urlopen('http://python.org/')
#response = urlopen(url)
#html = response.read()
#print(html)

str = quote('한글')
params=urlencode( (('v',1.0),
                   ('q',text),
                   ('langpair',langpair),) )
url = "https://translate.google.co.kr/#auto/ko/" + str
url = "http://ajax.googleapis.com/ajax/services/language/translate" + str
#url = 'http://wikipedia.org/wiki/' + quote("한글")
content = urlopen(url).read()
print(content)
