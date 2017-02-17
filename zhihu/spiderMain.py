# -*- coding: utf-8 -*
import downloader
from zhihu import imgOutputer
from zhihu import loginer
from zhihu import proxyManager
from zhihu import urlManager


class SpiderMain:
    def __init__(self):
        self.login = loginer.loginManager()
        self.downloader = downloader.Downloader()
        self.urls = urlManager.UrlMamaner()
        self.proxy = proxyManager.ProxyManager()
        self.imgOuter = imgOutputer.ImgOutputer()
        pass

    def crawl(self, my_topic):
        # 登入知乎

        # 通过话题获取url列表

        # 通过下载器下载每个页面数据

        # 抓取每个页面中的图片

        pass


if __name__ == "__main__":
    print u" ********知乎爬虫启动********* "
    topic = raw_input(u"请输入你感兴趣的话题 :  ")
    spider = SpiderMain()
    # 开启爬虫
    spider.crawl(topic)










