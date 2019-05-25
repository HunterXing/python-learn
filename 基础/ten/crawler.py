# 明确目的
# 分析网页
# 找到数据所在结构位置

# 模拟http请求 获取数据
# 正则筛选数据
# <div class="info"></div>
from urllib import request
import re
# 断点调试
class Spider:
    url = "https://www.huya.com/g"
    root_pattern = '<h3 class="title">([\s\S]*?)</h3>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls
    def __analysis(self, htmls):
        # return 1
        root_html = re.findall(Spider.root_pattern, htmls)
        return root_html
        # a = 1

    def go(self):
        htmls =  self.__fetch_content()
        html = self.__analysis(htmls)
        return html
        
spider = Spider()
result = spider.go()
print(result)