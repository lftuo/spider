import urllib2
class HttpRedirecHandlerTest(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(self,req,fp,code,msg,headers)
        result.status = code
        result.newurl = result.geturl()
        return result
opener = urllib2.build_opener(HttpRedirecHandlerTest)
opener.open('https://nj.lianjia.com/')