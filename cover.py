import urllib.request
import zlib
from lxml import etree
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
tar=input()
req=urllib.request.Request(url='https://www.bilibili.com/video/av'+tar,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'})
response=urllib.request.urlopen(req)
content=response.read()
content=zlib.decompress(content, 16+zlib.MAX_WBITS)
text=content.decode('utf-8') 
tree = etree.HTML(text)
result=tree.xpath('/html/head/meta[@itemprop="image"]/@content')
urllib.request.urlretrieve(result[0],filename=tar+".jpg")
print("已保存：av"+tar)