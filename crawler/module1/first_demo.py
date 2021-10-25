"""
@author:ming
@file:first_demo.py
@time:2021/10/21
"""

from urllib.request import urlopen

# 爬取百度的页面
response = urlopen("http://www.baidu.com")
print(type(response))
text = response.read().decode("utf-8")
# with open("baidu.html", mode="w", encoding="utf-8") as f:
#     f.write(text)
