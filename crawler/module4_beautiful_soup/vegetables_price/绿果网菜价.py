"""
@author:ming
@file:绿果网菜价.py
@time:2021/10/25
"""
import requests
from bs4 import BeautifulSoup
import csv
import time

"""
抓取绿果网的菜价
"""
# 拼接文件名
localtime = time.localtime(time.time())
file_name = "price_data_" + str(localtime.tm_year) + "-" + str(localtime.tm_mon) + "-" + str(
    localtime.tm_mday) + "-" + str(
    localtime.tm_hour) + "-" + str(
    localtime.tm_min) + ".csv"
# 打开存放数据的文件
price_data = open(file_name, mode='a', encoding="utf-8")
writer = csv.writer(price_data)
# with open("绿果网.html", mode="w", encoding="utf-8") as price_file:
#     price_file.write(response.text)

base_url = "https://www.lvguo.net"
try:
    # 获取前10页数据
    for i in range(1, 11):

        url = "t" + str(i)
        response = requests.get(f"{base_url}/baojia/%E8%94%AC%E8%8F%9C/6000/{url}")
        response.encoding = "UTF-8"
        response.close()

        # 用beautifulSoup解析,并指定使用html解析器
        page = BeautifulSoup(response.text, "html.parser")
        """
        page.find(标签，属性) 找到第一个符合条件的数据
        page.find(标签，attrs={
         "属性":"值"
        })
        page.find_all(标签，属性) 找到所有符合条件的数据
        """
        # 通过table标签找到数据表
        table = page.find("table")
        # 通过tr标签找到每一行数据，并切掉前两行
        table_rows = table.find_all("tr")[2:]
        # 遍历每一行
        for row in table_rows:
            # 通过td标签找到每一行的的每一列数据
            tds = row.find_all("td")
            # 存放每列的价格数据
            prices = []
            # tds[index].text 表示标签包裹的文本内容
            # 处理第4个标签里面的多个价格，封装成列表，找到所有的符合条件的<p>标签
            price_texts = tds[3].find_all("p", style="color:#3a8101; font-size:16px;")
            # 遍历价格列表
            for item in price_texts:
                prices.append(item.text.lstrip())

            # 处理详情链接
            details = tds[5].find("a")
            # 通过get()获取标签属性值
            details_url = details.get("href")

            t = tds[0].text
            place = tds[1].text
            name = tds[2].text
            producer = tds[4].text
            details_href = base_url + details_url
            # 写入一行数据
            writer.writerow([t, place, name, prices, producer, details_href])
        print("第", i, "页数据获取成功")
        time.sleep(0.5)
except Exception as e:
    print(e)
finally:
    # 关闭文件
    price_data.close()
