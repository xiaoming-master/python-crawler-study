"""
@author:ming
@file:re_test.py
@time:2021/10/23
"""
import re

# 匹配字符串中所有符合规则的内容，返回一个列表
res_list = re.findall(r"\d+", "我的电话号码是10086,他的电话号码是10010")
print(res_list)  # ['10086', '10010']

# 匹配字符串中所有符合规则的内容，返回一个迭代器对象
res_ite = re.finditer(r"\d+", "我的电话号码是10086,他的电话号码是10010")
for item in res_ite:
    print(item.group())  # item是一个Match对象，使用group()方法可以获取具体内容

# 匹配字符串中第一个符合规则的内容，返回一个Match对象
res_search = re.search(r"\d+", "我的电话号码是10086,他的电话号码是10010")
print(res_search.group())  # 10086

# 匹配字符串开头符合规则的内容（类似于start_with()函数），返回Match对象
res_match = re.match(r"\d+", "我的电话号码是10086,他的电话号码是10010")
print(res_match)  # None

res_match = re.match(r"\d+", "10086,他的电话号码是10010")
print(res_match.group())  # 10086

# 预加载正则表达式
rule = re.compile(r"\d+")

# 匹配字符串中所有符合规则的内容，返回一个列表
res_list = rule.findall("我的电话号码是10086,他的电话号码是10010")
print(res_list)  # ['10086', '10010']

res = rule.search("我的电话号码是10086,他的电话号码是10010")
print(res.group())  # 10086
