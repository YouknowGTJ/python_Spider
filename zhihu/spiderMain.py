# -*- coding: utf-8 -*
import downloader
from zhihu import imgOutputer
from zhihu import login_tool
from zhihu import proxyManager
from zhihu import urlManager


class SpiderMain:
    def __init__(self):
        self.loginer = login_tool.loginManager()
        self.downloader = downloader.Downloader()
        self.urls = urlManager.UrlMamaner()
        self.proxy = proxyManager.ProxyManager()
        self.imgOuter = imgOutputer.ImgOutputer()
        pass

    def crawl(self, my_topic):
        # 获取用户账号密码
        # account = raw_input(u"请输入您的知乎账号 :  ")
        # password = raw_input(u"请输入密码 :  ")
        account = "13738618437"
        password = "tianjiezzz"
        # 登入知乎
        self.loginer.login(account, password)
        # 通过话题获取url列表

        # 通过下载器下载每个页面数据

        # 抓取每个页面中的图片

        pass


if __name__ == "__main__":
    print u" ********知乎爬虫启动********* "
    #topic = raw_input(u"请输入你感兴趣的话题 :  ")
    topic = "爬虫"
    spider = SpiderMain()
    # 开启爬虫
    spider.crawl(topic)










