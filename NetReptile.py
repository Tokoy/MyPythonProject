# coding=utf-8
import re
import urllib

url = r'http://www.heibanke.com/lesson/crawler_ex00/'
reg = re.compile(r"<h3>[^\d<]*?(\d+)[^\d<]*?</h3>")

while True:
    print '正在读取网址', url
    html = urllib.urlopen(url).read()
    num = reg.findall(html)
    if len(num) == 0:
        break
    else:
        url = r'http://www.heibanke.com/lesson/crawler_ex00/'
        url = url+num[0]

print '结束'
