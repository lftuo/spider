import requests
postdata = {'key':'value'}
r = postdata.post('https://www.zhihu.com/#signin',data=postdata)
print r.content

