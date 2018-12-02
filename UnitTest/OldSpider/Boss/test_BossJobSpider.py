from DioSpider.OldSpider.Boss.BossJobSpider import BossJobSpider


def test_BossJobSpider():
    enterUrl = "https://www.zhipin.com/job_detail/3265d372b1182c951HR50t2-ElU~.html"
    for msg in BossJobSpider().crawl(enterUrl, {}):
        print(msg)