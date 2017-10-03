import requests
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0)'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.baidu.com',headers=headers)
print r.content