# -*- coding: utf-8 -*
import re

from zhihu.login_tool import head


class UrlMamaner(object):
    def __init__(self):
        self.question_url = []
        self.answer_url = []
        pass

    def get_url(self, topic, session):
        # 获取问题列表
        question_url = "https://www.zhihu.com/search?type=content&q="+topic
        response = session.get(question_url)
        state_code = response.status_code
        print u"爬虫报告：获取问题列表状态 ： " + str(state_code)
        text = response.text
        # ex : <a target="_blank" class="question_link" href="/question/49995249">爬虫，如何突破Incapsula保护的网站？</a>
        pattern = re.compile(r'href="/question/(.*?)"', re.S)
        question = re.findall(pattern, text)
        print question
        # 获取问题列表
        pass

