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
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    "User-Agent": agent
    }


class loginManager:
    def __init__(self):
        self.session = requests.session()
        self.session.headers = head
        self.cookies = requests.cookies.RequestsCookieJar()
        try:
            self.session.cookies.update(self.cookies)
        except Exception, e:
            print e
            print u"爬虫报告:cookies 未能加载..."

    # 获取全局会话对象
    def get_session(self):
        return self.session

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
        try:
            result = self.session.get(url, headers=head, allow_redirects=False)
            code = result.status_code
        except Exception, e:
            print e
            print u"爬虫报告:测试登入状态时遇到了一点小问题..."
            return False
        if 200 == code:
            print result.text
            return True
        else:
            return False

    def do_login(self, account, password):
        # 根据输入的账号获取URL和表单数据
        post_url, form_data = self.check_account(account, password)
        # 登入知乎
        try:
            login_page = self.session.post(post_url, data=form_data, head=head)
            login_code = login_page.status_code
            print u"爬虫报告：登入状态 : "+str(login_page)
        except :
            print u"需要验证码登入"
            pass

    def check_account(self, account, password):
        # 区分是电话号码登入还是邮箱账号登入
        if re.match(r"^1\d{10}$", account):
            print u"爬虫报告：您正使用手机账号登入..."
            login_url = "https://www.zhihu.com/login/phone_num"
            form_data = {
                "_xsrf": self.get_xsrf(),
                "password": password,
                "phone_num": account
            }
            return  login_url, form_data
        else:
            if "@" in account:
                print u"爬虫报告：您正使用邮箱账号登入..."
                login_url = "https://www.zhihu.com/login/email"
                form_data = {
                    "_xsrf": self.get_xsrf(),
                    "password": password,
                    "email": account
                }
                return login_url, form_data
            else:
                print u"爬虫报告：您输入的账号有误，请输入手机账号or邮箱账号..."
                return None, None

    def get_xsrf(self):
        index_url = "https://www.zhihu.com/#signin"
        html = self.session.get(index_url, heads=head).text
        if html is not None:
            _xsrf = re.match(r'name="_xsrf" value="(.*?)"', html)
            return _xsrf.group(1)



