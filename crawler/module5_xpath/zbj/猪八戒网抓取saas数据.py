"""
@author:ming
@file:猪八戒网抓取saas数据.py
@time:2021/10/26
"""
import requests
from lxml import etree
import csv

"""
在搜索栏搜索saas抓取搜索结果
"""
kw = "saas"
url = f"https://nanchong.zbj.com/search/f/?kw={kw}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
# 访问获取响应
response = requests.get(url, headers=headers)
response.encoding = "utf-8"
response.close()
# with open("猪八戒.html", mode='w', encoding="utf-8") as zbj_file:
#     zbj_file.write(response.text)

# 存放数据
data = []
# 统计
count = 0
# xpath解析
tree = etree.HTML(response.text)
# 从根标签查找到所有的商品外层div
product_divs = tree.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
for div in product_divs:
    # 通过标签层次查找数据
    # /text() 用于获取标签内的文本
    # /tag[@属性：值] 限定标签的属性值
    # /tag/@属性 获取标签的属性值
    shop_name = div.xpath("./div/div/a[1]/div[1]/p/text()")[1].strip()
    place = div.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]
    price = div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0][1:]
    title = kw.join(div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
    data.append([shop_name, title, price, place])
    count += 1
    print("找到第", count, "条数据:", "店铺名:", shop_name, ",价格: ￥", price)
with open("zbj_" + kw + "_data.csv", mode="w", encoding="utf-8") as data_file:
    writer = csv.writer(data_file)
    writer.writerows(data)
print("写入文件完成")
