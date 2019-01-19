import requests
import urllib.request

def search(link,avnum):
    data=requests.get(link).content.decode('utf-8')
    import re
    pat="http://.{2}\.hdslb.com/bfs/archive/.+?\.jpg"
    pattern=re.compile(pat)
    result=pattern.findall(data)
    return urllib.request.urlretrieve(result[0],filename=avnum+".jpg")

print("av")
avnum=input()
link="https://www.bilibili.com/video/av"+avnum
print("Complete:"+str(search(link,avnum)))