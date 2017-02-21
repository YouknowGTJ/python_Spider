# -*- coding: utf-8 -*
import re

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
        self.cookies = requests.cookies.RequestsCookieJar()
        try:
            self.session.cookies.update(self.cookies)
        except:
            print u"爬虫报告:cookies 未能加载..."

    # 登入知乎
    def login(self, account, password):
        if self.is_login():
            print u"爬虫报告:你已成功登入知乎..."
        else:
            print u"爬虫报告:正在努力登入知乎..."
            self.do_login(account, password)

    # 测试是否已经登入
    def is_login(self):
        url = "https://www.zhihu.com/people/edit"
        result = self.session.get(url, headers=head, allow_redirects=False ).status_code
        if 200 == result:
            return True
        else:
            return False

    def do_login(self, account, password):
        # 区分是电话号码登入还是邮箱账号登入
        if re.match(r"^1\d{10}$", account):
            url = "https://www.zhihu.com/login/phone_num"
            form_data = {
            "_xsrf": self.get_xsrf(),
            "password": password,
            "phone_num": account,
            }
        else:
            pass
        pass

    def get_xsrf(self):
        index_url = "https://www.zhihu.com/#signin"
        html = self.session.get(index_url, heads=head).text
        if html is not None:
            _xsrf = re.match(r'name="_xsrf" value="(.*?)"', html)
            return _xsrf.group(1)



