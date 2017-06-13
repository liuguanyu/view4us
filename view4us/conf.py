# -*- coding: utf-8 -*-

# 最热电视剧列表
LIST_PLAY_INDEX = {
    "全部": "http://top.baidu.com/buzz?b=4&c=2&fr=topcategory_c2",
    "偶像": "http://top.baidu.com/buzz?b=349&c=2&fr=topbuzz_b4_c2",
    "言情": "http://top.baidu.com/buzz?b=350&c=2&fr=topbuzz_b349_c2",
    "古装": "http://top.baidu.com/buzz?b=351&c=2&fr=topbuzz_b350_c2",
    "伦理": "http://top.baidu.com/buzz?b=448&c=2&fr=topbuzz_b448_c2",
    "美剧": "http://top.baidu.com/buzz?b=452&c=2&fr=topbuzz_b448_c2",
    "韩剧": "http://top.baidu.com/buzz?b=453&c=2&fr=topbuzz_b452_c2",
    "日剧": "http://top.baidu.com/buzz?b=466&c=2&fr=topbuzz_b453_c2",
    "港剧": "http://top.baidu.com/buzz?b=464&c=2&fr=topbuzz_b466_c2",
    "台剧": "http://top.baidu.com/buzz?b=465&c=2&fr=topbuzz_b464_c2",
    "泰剧": "http://top.baidu.com/buzz?b=467&c=2&fr=topbuzz_b465_c2"
}

# 请求头
HEADERS = [{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
    {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]

MAX_RETRY = 3    