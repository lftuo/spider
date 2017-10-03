import chardet
import requests
r = requests.get('http://www.baidu.com')
print chardet.detect(r.content)
r.encoding = chardet.detect(r.content)['encoding']
print r.text