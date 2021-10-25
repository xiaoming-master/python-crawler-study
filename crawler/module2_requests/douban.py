"""
@author:ming
@file:douban.py
@time:2021/10/21
"""

import requests

"""
豆瓣网爬取热门电影
"""

headers = {
    "Connection": "keep-alive",
    "Cookie": "ll=\"118328\"; bid=k-4RvnIkCmY; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1634815608%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3D%25E8%25B1%2586%25E7%2593%25A3%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; _vwo_uuid_v2=DAC64A6231942B13980E591294D555031|67dc8f62c8af80ed62143203e2bc6fdb; dbcl2=\"248790181:L / vx94Nhiyw\"; ck=uJXo; push_noty_num=0; push_doumail_num=0; __gads=ID=2a8dc11ec04c2f99:T=1634817066:S=ALNI_MZ1zB3UVBTkMip59dqJdv31eBj20g; _pk_id.100001.4cf6=d22b6aba51afdad6.1634815608.1.1634817142.1634815608.",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}
start = 0
res = dict()
for i in range(1):
    start += 20 * i
    params = {
        "sort": "U",
        "range": "0,10",
        "tags": "",
        "start": start,
    }
    response = requests.get("https://movie.douban.com/j/new_search_subjects", headers=headers, params=params)
    with open("hot_movie.json", mode="w") as hot_movie:
        hot_movie.write(response.text)
    # if res:
    #     print(res.get("data"))
        # res["data"] = res.get("data").extend(response.json().get("data"))

    # else:
    #     res = response.json()
    response.close()

print("ok")
