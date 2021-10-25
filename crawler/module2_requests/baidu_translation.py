"""
@author:ming
@file:baidu_translation.py
@time:2021/10/21
"""
"""
百度翻译爬取
"""

import requests

query = input("请输入需要翻译的英文:")
data = {
    "kw": query

}

response = requests.post("https://fanyi.baidu.com/sug", data=data)
print(response.json())
