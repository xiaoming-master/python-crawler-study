"""
@author:ming
@file:龙部落热门推荐.py
@time:2021/10/23
"""

import re
import requests
import json

print("开始抓取>>>>>>>>")
# 主页url
home_page_url = "https://www.longbulo.com/"
# 播放根地址
play_base_url = home_page_url + "video"

# 获取主页数据
home_page_response = requests.get(home_page_url)
# 设置页面编码
home_page_response.encoding = "utf-8"
home_page_response.close()
home_page_content = home_page_response.text
# 保存主页到文件
# with open("home_page.html", mode="w", encoding="utf-8") as home_page:
#     home_page.write(home_page_content)

# 热门推荐匹配规则
home_page_rule = re.compile('<h3>热门推荐</h3>.*?<ul>(?P<recommend_list>.*?)</ul>', re.S)
# 获取链接规则
home_page_recommend_urls_rule = re.compile(
    '<li><span .*?>.*?</span><h4><a href="(?P<url>.*?)" target="_blank">.*?</a></h4></li>', re.S)
content_rule = re.compile('''<div class="info fl">
            <h1>(?P<movie_name>.*?)</h1>
            <p>类型：<span><a href=".*?" target="_blank">(?P<movie_type>.*?)</a></span></p>
            <p>地区：<span>(?P<movie_region>.*?)</span></p>
            <p>年代：<span>(?P<movie_year>.*?)</span></p>
            <p>导演：<span>(?P<movie_director>.*?)</span></p>
            <p class="long">主演：<span>.*?</span></p>
            <p class="playlisturl"><a href="(?P<play_url>.*?)" target="_blank">.*?</a></p>
        </div>''')

# 用于存放链接的列表
urls = []
# 统计影视作品数量
count = 0
# 存放影视作品信息
movies = []

# 匹配获取链接
recommendation = home_page_rule.finditer(home_page_content)
# 有三个热门推荐，分别遍历
for item in recommendation:
    # 将热门推荐读取
    recommendation_content = item.group("recommend_list").lstrip()
    # 遍历热门推荐，提取链接
    for content in home_page_recommend_urls_rule.finditer(recommendation_content):
        # 将url放入到列表中
        urls.append(content.group("url"))

# 遍历url列表，获取影视资料
for url in urls:
    # 拼接链接
    link = home_page_url + url
    # 访问链接接
    content_res = requests.get(link)
    content_res.close()
    # 设置编码
    content_res.encoding = "utf-8"
    movie_infos = content_rule.finditer(content_res.text)
    for info in movie_infos:
        movie_name = info.group("movie_name")
        movie_type = info.group("movie_type")
        movie_region = info.group("movie_region")
        movie_year = info.group("movie_year")
        movie_director = info.group("movie_director")
        play_url = info.group("play_url")
        movie = {
            "movie_name": movie_name,
            "movie_type": movie_type,
            "movie_region": movie_region,
            "movie_year": movie_year,
            "movie_director": movie_director,
            "play_url": play_base_url + play_url
        }
        # 储存到列表
        movies.append(movie)
        count += 1
        print("发现第", count, "个影视作品:", movie_name)
print("写入文件中>>>>>>>>")
with open("hot_movies.json", mode="w", encoding="utf-8") as hot_movie_file:
    json.dump(movies, fp=hot_movie_file, ensure_ascii=False)
print("写入完!")
