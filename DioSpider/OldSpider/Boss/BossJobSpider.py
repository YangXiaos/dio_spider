# @Time         : 18-12-2 下午7:24
# @Author       : DioMryang
# @File         : BossContentSpider.py
# @Description  :
from DioCore.Downloader.Downloader import Downloader
from DioCore.Utils import TextUtil, DateTimeUtil
from DioFramework.Base.Message import Message
from DioFramework.Base.Spider.LocalSpider import LocalRegexSpider


class BossJobSpider(LocalRegexSpider):
    """
    boss搜索爬虫
    """
    regex = "https://www.zhipin.com/c\d+/?query=.*&period=\d+&ka=sel-scale-\d+"

    def crawl(self, enterUrl, info):
        res = Downloader.getWithBs4(enterUrl)

        text = res.soup.select(".detail-content .text")
        msg = Message(info=info)
        msg.updateInfo({
            "_id": TextUtil.getFirstMatch(res.text, "job_id: '(.*?)',"),
            "job_name": TextUtil.getFirstMatch(res.text, "job_name: '(.*?)',"),
            "job_salary": TextUtil.getFirstMatch(res.text, "job_salary: '(.*?)',"),
            "company": TextUtil.getFirstMatch(res.text, "company:'(.*?)',"),
            "city": TextUtil.getFirstMatch(res.text, "<p>城市：(.*?)<em class=\"vline\">"),
            "work_year": TextUtil.getFirstMatch(res.text, "<\/em>经验：(.*?)<em class=\"vline\">"),
            "pubDate": DateTimeUtil.getStandardDatetime(DateTimeUtil.guess(
                    TextUtil.getFirstMatch(res.text, "\"pubDate\": \"(\d+-\d+-\d+T\d+:\d+:\d+)\","))),
            "upDate": DateTimeUtil.getCurStandardDate(),
            "hr": res.soup.select_one("h2.name").text,

            "job_description": text[0].text.strip(),
            "company_introduction": res.soup.select(".detail-content .text")[1].text.strip() if len(text) >=2 else "",
        })

        yield msg

