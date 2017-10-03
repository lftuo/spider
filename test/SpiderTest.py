import urllib2
response=urllib2.urlopen('https://github.com/login')
html=response.read()
print html