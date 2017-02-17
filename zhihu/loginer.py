# -*- coding: utf-8 -*
import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib

#  generate request head
agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
head = {
    "Host:", "www.zhihu.com"
    "Referer:", "https://www.zhihu.com/"
    "User-Agent:", agent
    }


class loginManager:
    def __init__(self):
        self.session = requests.session()
        self.session.cookies = cookielib.LWPCookieJar(filename="cookies")
        try:
            self.session.cookies.load()
        except:
            print u"cookies 未能加载..."

    # 登入知乎
    def login(self, account, password ):
        self.is_login()

    # 测试是否已经登入
    def is_login(self):

        pass



