"""
@author:ming
@file:优美图库图片.py
@time:2021/10/25
"""
"""
优美图库图片抓取
"""
import requests
from bs4 import BeautifulSoup

base_url = "https://www.umei.cc"
url = base_url + "/bizhitupian/diannaobizhi"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
# 访问获取响应
main_page_response = requests.get(url, headers)
# 设置编码
main_page_response.encoding = "utf-8"
main_page_response.close()

# beautifulSoup解析
main_page_soup = BeautifulSoup(main_page_response.text, "html.parser")
# 获取div内的图片链接数据
img_list_div = main_page_soup.find("div", class_="TypeList")
# 获取a标签
click_links_a = img_list_div.find_all("a")
# 存放详情页面链接
links = []
# 遍历a标签
for a in click_links_a:
    # 获取a标签href属性的值
    href = base_url + a.get("href")
    # 保存
    links.append(href)

# 存放图片链接
imgs_info = []
# 进入详情页面，获取高清图的链接
for link in links:
    # 访问详情链接
    detail_page_response = requests.get(link, headers)
    detail_page_response.encoding = "utf-8"
    detail_page_response.close()
    # BeautifulSoup解析
    detail_page_soup = BeautifulSoup(detail_page_response.text, "html.parser")
    # 获取p标签
    p = detail_page_soup.find("p", align="center")
    # 获取img标签
    img_tag = p.find("img")
    # 获取图片链接
    img_src = img_tag.get("src")
    # 图面文件名格式
    suffix = img_src.split(".")[-1]
    # 获取并拼接图片名称
    img_name = detail_page_soup.find("h1", class_="inline").text + "." + suffix
    img = {
        "name": img_name,
        "src": img_src
    }
    imgs_info.append(img)

# 打开下载目录
# 下载图片
for img in imgs_info:
    # 访问图片链接
    img_response = requests.get(img.get("src"), headers)
    img_response.close()
    # 获取响应二进制数据
    img_content = img_response.content
    # 获取文件名
    with open("img/" + img.get("name"), mode="wb") as img_file:
        img_file.write(img_content)
    print(img.get("name"), "下载完成")
