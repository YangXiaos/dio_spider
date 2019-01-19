# @Time         : 18-12-2 下午4:02
# @Author       : DioMryang
# @File         : BossSearchCrawler.py
# @Description  :
from DioCore.Network.Downloader.Downloader import Setting, Downloader
from DioFramework.Base.Message import Message
from DioFramework.Base.Spider.LocalSpider import LocalRegexSpider


class BossSearchSpider(LocalRegexSpider):
    """
    boss搜索爬虫
    """
    regex = "https://www.zhipin.com/c\d+/?query=.*&period=\d+&ka=sel-scale-\d+"

    def crawl(self, enterUrl, info):
        setting = Setting()
        setting.htmlParse = True
        res = Downloader.get(enterUrl, setting)

        for aTag in res.soup.select(".info-primary h3 a"):
            yield Message(info={"enter_url": "https://www.zhipin.com" + aTag["href"]})


