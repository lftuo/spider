import requests
r = requests.get('http://www.baidu.com')
print 'content--->'+r.content
print 'text--->'+r.text
print 'encoding--->'+r.encoding
r.encoding = 'utf-8'
print 'new text--->'+r.text