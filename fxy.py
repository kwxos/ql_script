import os
import requests
import datetime
import json

pushplus_token = os.environ.get('pg_pushplus_token')
fxy_cookie = os.environ.get('fxy_cookie')
def baoh():
    url1 = "https://cloud.revcloud.tech/clientarea"
    headers1 = {
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "DNT": "1",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://cloud.revcloud.tech",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6",
        "Cookie": fxy_cookie
    }
    response1 = requests.get(url1, headers=headers1)
    if response1.ok:
        print("保活中...")

def qiand():
    url = "https://cloud.revcloud.tech/addons"
    params = {
        "_plugin": "23",
        "_controller": "index",
        "_action": "index"
    }
    headers = {
        "Host": "cloud.revcloud.tech",
        "Connection": "keep-alive",
        "Content-Length": "7",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "sec-ch-ua-mobile": "?0",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "DNT": "1",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://cloud.revcloud.tech",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://cloud.revcloud.tech/addons?_plugin=23&_controller=index&_action=index",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6",
        "Cookie": fxy_cookie
    }
    datac = {
        "uid": "783",
        "type": "point"
    }
    dataq = {
        "uid": "783",
    }
    responseq = requests.post(url, headers=headers, params=params, data=dataq)
    responsec = requests.post(url, headers=headers, params=params, data=datac)
    print(responseq.text)
    print(responsec.text)
    data12q=json.loads(responseq.text)
    data12c=json.loads(responsec.text)
    pmsg=f"{data12q["msg"]}\n{data12c["msg"]}"
    print(pmsg)
    try:
        url = 'https://www.pushplus.plus/send/'
        data = {
            "token": pushplus_token,
            "title": '复兴云签到',
            "content": pmsg
        }
        re = requests.post(url, json=data)
        msg = re.json().get('msg', None)
        print(f'pushplus推送结果：{msg}\\\n')
    except Exception as e:
        print(f"pushplus推送出现错误: {e}")

now = datetime.datetime.now()
# 判断是否在 16:30 到 16:50 之间
if now.hour == 16 and 30 <= now.minute <= 50:
    qiand()  # 如果在 16:30-16:50 之间，执行 qiand() 函数
else:
    baoh()  # 否则执行 baoh() 函数
