#!/usr/bin/python
import requests
import  json
headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "165",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie":"GAME_ID=12000119; GAME_NAME=nba; connect.sid=s%3AKhw44X1K5KwcxePZQNg7hwOg.tUAV5vkg7zkq14%2BfA%2FPYteGPUgMPNVsZStlMfzACSBk",
    "Host": "web4-nba.mobage.cn:8888",
    "Origin": "http://web4-nba.mobage.cn:8888",
    "Referer": "http://web4-nba.mobage.cn:8888/addItem",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
}

#headers['User-Agent']="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
id="1138355187514944170"
server=4
data={
    'game_user_id': id,
    'server_id': server,
    "giftList": {"10694": 1},
    'message': 1,
    'comment': 1,
    'submit': 'Submit'
}
data=json.dumps(data)
url="http://web4-nba.mobage.cn:8888/addItem"
response=requests.post(url="http://web4-nba.mobage.cn:8888/addItem",headers=headers,data=data,timeout=20)
# response=requests.get(url=url,headers=headers,params=data)
print response.status_code
# print response.json
print response.text

# rs=requests.get("http://web4-nba.mobage.cn:8888/addItem")
# print rs.cookies
