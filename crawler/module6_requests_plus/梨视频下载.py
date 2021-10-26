"""
@author:ming
@file:梨视频下载.py
@time:2021/10/26
"""

import requests

# https://www.pearvideo.com/video_1744464 页面链接
# https://video.pearvideo.com/mp4/adshort/20211025/cont-1744464-15787050_adpkg-ad_hd.mp4 播放链接
# https://video.pearvideo.com/mp4/adshort/20211025/cont-1744464-15787050_adpkg-ad_hd.mp4
# https://video.pearvideo.com/mp4/adshort/20211025/1635257300512-15787050_adpkg-ad_hd.mp4 后端返回链接，加密处理过
# 页面
cont_id = "1744193"
page_url = f"https://www.pearvideo.com/video_{cont_id}"
video_status_url = f"https://www.pearvideo.com/videoStatus.jsp?contId={cont_id}&mrd=0.5267971241406777"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    # 防盗链，访问当前链接的页面地址
    "Referer": page_url
}
video_status_resp = requests.get(video_status_url, headers=headers)
video_status_resp.close()
video_status = video_status_resp.json()
# 响应的系统时间
system_time = video_status["systemTime"]
# 响应的加密播放链接
src_url = video_status["videoInfo"]["videos"]["srcUrl"]
# 解密
download_url = src_url.replace(system_time, "cont-" + cont_id)
# 下载
print(download_url)
source_resp = requests.get(download_url, headers=headers)
with open("videos/" + cont_id + ".mp4", mode="wb") as video_file:
    video_file.write(source_resp.content)
source_resp.close()
print("下载完成")
