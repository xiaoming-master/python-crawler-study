"""
@author:ming
@file:青春有你学员.py
@time:2021/10/23
"""
import requests
import re
import json

# 请求头，防止爬虫被拦截
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
# 百度百科的链接
url = "https://baike.baidu.com/item/%E9%9D%92%E6%98%A5%E6%9C%89%E4%BD%A0%E7%AC%AC%E4%BA%8C%E5%AD%A3"
# 请求，并获取响应
response = requests.get(url, headers=headers)
# 关闭连接
response.close()
# 获取响应中的html文本
data = response.text
# 预加载正则表达式
pattern = re.compile(
    r'''<tr><td align="center" width="95"><div class="para" label-module="para"><a .*?>(?P<name>.*?)</a></div></td><td align="center" width="109"><div class="para" label-module="para">(?P<country>.*?)</div></td><td align="center" width="79"><div class="para" label-module="para">(?P<constellation>.*?)</div></td><td valign="top" align="left" width="413"><div class="para" label-module="para">(?P<slogan>.*?)</div></td><td align="center" width="158"><div class="para" label-module="para">(?P<company>.*?)</div></td></tr>''',
    re.S)
# 匹配
singer_msg = pattern.finditer(data)

students_msg = []
count = 0
# 获取匹配的结果
for msg in singer_msg:
    count += 1
    name = msg.group("name")
    country = msg.group("country")
    constellation = msg.group("constellation")  # 星座
    slogan = msg.group("slogan")  # 花语
    company = msg.group("company")
    # 有的公司带有链接，需要进行过滤
    if company.startswith("<a"):
        company = re.search("<a .*?>(?P<company_with_not_link>.*?)</a>", company).group("company_with_not_link")
    # 封装成字典对象
    student = {
        "name": name,
        "country": country,
        "constellation": constellation,
        "slogan": slogan,
        "company": company,
    }
    # 放入到列表中
    students_msg.append(student)
    print("查找到第", count, "个学员:", name)

# 将学员信息写入文件
print("写入文件")
with open("青春有你学员.json", mode="w", encoding="utf-8") as f:
    # ensure_ascii=False 解决非ASCII码的数据乱码问题
    json.dump(students_msg, fp=f, ensure_ascii=False)
print("ok")

# 读取数据
# with open("青春有你学员.json", mode="r", encoding="utf-8") as f:
#     data = json.load(f)
#     for item in data:
#         print(item)

r"""
关于json.dumps() 的参数
Skipkeys：默认值是False，如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，
        设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key

ensure_ascii：默认值True，如果dict内含有non-ASCII的字符，则会类似\uXXXX的显示数据，设置成False后，就能正常显示

indent：应该是一个非负的整型，如果是0，或者为空，则一行显示数据，否则会换行且按照indent的数量显示前面的空白，
        这样打印出来的json数据也叫pretty-printed json，写几个数字，则前面留几个空格

separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(',',':')；
        这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“：”隔开。

encoding：默认是UTF-8，设置json数据的编码方式。

sort_keys：将数据根据keys的值进行排序。

Decode过程，是把json对象转换成python对象的一个过程，常用的两个函数是loads和load函数。区别跟dump和dumps是一样的
"""
