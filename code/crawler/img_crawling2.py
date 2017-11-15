#coding = utf-8
import os
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = 'src="(.+?\.jpg)" alt='
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    dir_path = 'img2/'
    if not os.path.exists(dir_path):
        os.makedirs('img2/')
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, dir_path+'%s.jpg' % x)
        x+=1
    return imglist

html = getHtml("http://pic.yxdown.com/list/0_0_1.html")

print getImg(html)