from DioSpider.OldSpider.Boss.BossSearchSpider import BossSearchSpider


def test_BossSearchSpider():
    enterUrl = "https://www.zhipin.com/c101280100/?query=%E7%88%AC%E8%99%AB&period=3&ka=sel-scale-3"
    for msg in BossSearchSpider().crawl(enterUrl, {}):
        print(msg)
    pass
