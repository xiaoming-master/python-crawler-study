"""
@author:ming
@file:re_test2.py
@time:2021/10/23
"""
import re

s = r"""
<div class='jay'><span id='1'>周杰轮</span></div>
<div class='abc'><span id='2'>jacke</span></div>
<div class='jj'><span id='3'>林俊杰</span></div>
<div class='nb'><span id='4'>ming</span></div>
<div class='df'><span id='5'>aaa</span></div>
"""

# (?P<分组名称>正则),可以单独从正则匹配到的内容中进一步提取内容 item.group('分组名称')
# re.S 让 . 可以匹配换行符
rule = re.compile(r"<div class='(.*?)'><span id='(?P<id>.*?)'>(?P<name>.*?)</span></div>", re.S)
res = rule.finditer(s)
for item in res:
    print("id =", item.group('id'), end="\t")
    print("name =", item.group('name'))
