import urllib2
request = urllib2.Request("https://gz.lianjia.com/ershoufang/GZ0003030524.html")
response = urllib2.urlopen(request)
html = response.read()
print html