"""
@author:ming
@file:requests_demo1.py
@time:2021/10/21
"""
import requests

# 添加请求头，防止反爬虫
# User-Agent会告诉网站服务器，访问者是通过什么工具来请求的，如果是爬虫请求，一般会拒绝，如果是用户浏览器，就会应答。
keywords = input("请输入百度的关键字：")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}
# 百度爬取taylor swift的检索信息
response = requests.get(f"https://www.baidu.com/s?wd={keywords}", headers=headers)

with open("baidu_res.html", mode="w", encoding="utf-8") as f:
    f.write(response.text)
print("ok!")
