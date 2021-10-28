"""
@author:ming
@file:代理.py
@time:2021/10/27
"""
import requests

"""
使用代理ip
"""
proxies = {
    "http": "http://120.24.213.6:8000"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
url = "http://www.baidu.com"
response = requests.get(url, headers=headers, proxies=proxies, verify=False)
response.encoding = "utf-8"
print(response.text)
response.close()
