import urllib2
response = urllib2.urlopen("https://gz.lianjia.com/ershoufang/GZ0003030524.html")
html = response.read()
print html