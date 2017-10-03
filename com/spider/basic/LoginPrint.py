import urllib2
request = urllib2.urlopen('https://github.com/login')
html = urllib2.urlopen(request)
print html