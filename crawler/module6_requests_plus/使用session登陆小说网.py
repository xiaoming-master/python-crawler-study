"""
@author:ming
@file:使用session登陆小说网.py
@time:2021/10/26
"""
import requests

login_url = "https://passport.17k.com/ck/user/login"
user_data = {
    "loginName": "17383653532",
    "password": "luo990922.."
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
# 获取session
session = requests.session()
# 登陆操作
login_response = session.post(login_url, data=user_data, headers=headers)
# 查看cookies
print(session.cookies)
# 查看书架 两种方式

# shelf_response = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919", headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
#     "Cookie": "GUID=c3c099ce-b12f-4ac9-883f-e23072d938a4; BAIDU_SSP_lcr=https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&ch=&tn=baidu&bar=&wd=%E5%B0%8F%E8%AF%B4%E7%BD%91&oq=csv.writerows&rsv_pq=d647a7ad000404d4&rsv_t=282byNfQkeaXhXQMmmp%2FJ5YBOCpkDH90zhDlGFOjpXVdkrBcBo%2F11Ek%2BHzQ&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=33&rsv_sug1=30&rsv_sug7=100; Hm_lvt_9793f42b498361373512340937deb2a0=1635251572; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F00%252F80%252F35%252F84333580.jpg-88x88%253Fv%253D1635251688000%26id%3D84333580%26nickname%3D%25E5%25B0%258F%25E6%2598%258EQAQ%26e%3D1650804233%26s%3D04be0458fde2aa8e; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2284333580%22%2C%22%24device_id%22%3A%2217cbc96cbbe97f-0c92efbcd81e1c-57b193e-1327104-17cbc96cbbfb4c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fs%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E5%B0%8F%E8%AF%B4%E7%BD%91%22%7D%2C%22first_id%22%3A%22c3c099ce-b12f-4ac9-883f-e23072d938a4%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1635253367"
# })
shelf_response = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
with open("book_shelf.json", mode="w", encoding="utf-8") as shelf_file:
    shelf_file.write(shelf_response.text)
login_response.close()
