# https://docs.python.org/3/library/configparser.html
'''
이 모듈을 테스트하기 위한 파일명을 configparser 라고 지으면 안됩니다.


# https://docs.python.org/3/library/configparser.html

[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg

[topsecret.server.com]
Port = 50022
ForwardX11 = no


'''

import configparser


config = configparser.ConfigParser()

print(config.sections())

config.read("..\\setting\\config.ini")

print (config.sections())

for key in config['bitbucket.org']:
    print(key)

print (config['bitbucket.org']['User'])

print(config['DEFAULT']['Compression'])



#
# config = configparser.ConfigParser()
# config['DEFAULT'] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Port'] = '50022'     # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('example.ini', 'w') as configfile:
#   config.write(configfile)
#
#
#
