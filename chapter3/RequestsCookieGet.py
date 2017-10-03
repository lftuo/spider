import requests
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; MAC OS)'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.baidu.com',headers = headers)
for cookie in r.cookies.keys():
    print cookie+":"+r.cookies.get(cookie)