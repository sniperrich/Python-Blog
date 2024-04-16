import requests
spurl=input("shurulianjie")
res=requests.get('https://jx.xmflv.com/?url='+spurl)
print(res.text)