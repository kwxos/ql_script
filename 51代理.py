import os

import requests
import time
import random
from datetime import datetime, timedelta

ip51_cookie = os.environ.get('51ip_cookie')
ip51_key = os.environ.get('51ip_key')
pushplus_token = os.environ.get('pg_pushplus_token')
heartbeat_url = 'https://m.51daili.com/wap/user/index.html'
signin_url = 'https://m.51daili.com/wap/user/signin.html'
sech=f"https://aapi.51daili.com/userapi?appkey={ip51_key}"

headers = {
    'Host': 'm.51daili.com',
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Origin': 'https://m.51daili.com',
    'User-Agent': '',
    'Connection': 'keep-alive',
    'Referer': 'https://m.51daili.com/wap/user/index.html',
    'Content-Length': '2',
    'Cookie': ip51_cookie
}

data = {}


def send_heartbeat():
    try:
        response = requests.post(heartbeat_url, json=data, headers=headers)
        print(f"{datetime.now()} - Status Code: {response.status_code}")
        print("保活成功")
    except requests.RequestException as e:
        print(f"{datetime.now()} - Error")


def send_signin():
    try:
        response = requests.post(signin_url, json=data, headers=headers)
        if response.status_code == 200:
            # print(response.json())
            print("签到完成")
        else:
            print(f"{datetime.now()} - Error")
    except requests.RequestException as e:
        print(f"{datetime.now()} - Error")

def send_seh():
    try:
        response = requests.get(sech, headers=headers)
        if response.status_code == 200:
            data1=response.json()['data']['currentScore']
            print(f"当前积分{data1}")
        else:
            print(f"{datetime.now()} - Error")
    except requests.RequestException as e:
        print(f"{datetime.now()} - Error")


now = datetime.now()
# 判断是否在 16:30 到 16:50 之间
if now.hour == 10 and 30 <= now.minute <= 50:
    send_signin()
    time.sleep(3)
    send_seh()
else:
    send_heartbeat()
