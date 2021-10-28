"""
@author:ming
@file:网易云音乐.py
@time:2021/10/27
"""
import json
import time
from concurrent.futures import ThreadPoolExecutor

import requests
from lxml import etree
from Crypto.Cipher import AES
from base64 import b64encode

"""
网易云音乐抓取
使用线程池优化下载
"""

base_url = "https://music.163.com"
headers = {
    # 防盗链
    "referer": "https://music.163.com/",
    "origin": "https://music.163.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
# 专辑id
album_id = input("请输入歌单id:")
# 播放列表url
playlist_url = f"https://music.163.com/playlist?id={album_id}"
playlist_resp = requests.get(playlist_url, headers)
playlist_resp.close()

# xpath解析
tree = etree.HTML(playlist_resp.text)
playlist_div = tree.xpath("""//*[@id="song-list-pre-cache"]""")[0]
song_li = playlist_div.xpath("./ul/li")

# 存放歌曲
song_list = []
for li in song_li:
    # 歌曲详情链接
    href = li.xpath("./a/@href")[0]
    # 通过链接获取id
    song_id = href.split("=")[-1]
    # 歌曲名称
    name = li.xpath("./a/text()")[0]
    song = {
        "name": name,
        "song_id": song_id,
        "href": href
    }
    song_list.append(song)

# 下载
# method=post data={params,encSecKey}
# params 加密过的参数
# encSecKey 密钥
download_url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="

i = "SEyAPJ4lrx3HaR6r"
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
# 密钥 i,e,f值不变，密钥不变
encSecKey = "67d292950cc8d780efe7eb0235bd0f07ba3d3dca2ca0c10bbc3edb3c68571e41adbd2ac1964b875749ea9769a98a22b7b608960e5d9441908678bf54bb0a912866a9dcf3d86088480504b7b093c017b2d09d9863a6d9d730ea5ace0cd41cb75108ea9ee5d8d4cb75f0ff3e366a8f6008b9da0976910c31d1b06dc0c5f3b846f8"


# 加密函数
# var bUM9D = window.asrsea(JSON.stringify(i8a), bsB3x(["流泪", "强"]), bsB3x(WX6R.md), bsB3x(["爱心", "女孩", "惊恐", "大笑"]));


# 把字符串长度加长到16的倍数
def to_16(data):
    dv = 16 - len(data) % 16
    data += chr(dv) * dv
    return data


# a要加密的数据
# b 密钥
def crypt_data(a, b):
    # 获取字节码
    # 待加密数据
    a = to_16(a)
    a_byte = a.encode("utf-8")
    # 密钥
    b_byte = b.encode("utf-8")
    # 偏移量
    d_byte = "0102030405060708".encode("utf-8")
    aes = AES.new(b_byte, AES.MODE_CBC, IV=d_byte)
    # 加密
    res = aes.encrypt(a_byte)
    # 转化为字符串
    return str(b64encode(res), "utf-8")


# 加密数据
def get_enc_text(a):
    first_crypt = crypt_data(a, g)
    second_crypt = crypt_data(first_crypt, i)
    return second_crypt


# 封装下载函数
def download(song):
    song_ids[0] = song["song_id"]
    # 真实的参数
    real_params = {
        "csrf_token": "",
        "encodeType": "aac",
        "ids": song_ids,
        "level": "standard"
    }
    # 加密
    params = get_enc_text(json.dumps(real_params))
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    # 请求获取播放链接
    song_msg_resp = requests.post(download_url, data=data, headers=headers)
    song_msg_resp.close()
    # 解析响应
    song_msg = song_msg_resp.json()
    song_detail = song_msg["data"][0]
    # 下载
    if song_detail["url"]:
        # 访问下载链接
        song_content_resp = requests.get(song_detail["url"], headers)
        file_name = "song/" + song["name"] + "." + song_detail['type']
        with open(file_name, mode="wb") as song_file:
            # 写入文件
            song_file.write(song_content_resp.content)
        song_content_resp.close()
        # 休息一秒
        return song["name"]


# 创建线程池
executor = ThreadPoolExecutor(20)
# 歌曲id
song_ids = [1] * 1  # 长度为1的列表
futures = [executor.submit(download, song=song) for song in song_list]
for future in futures:
    print("《" + str(future.result()) + "》", "下载完成")
print("over!")
