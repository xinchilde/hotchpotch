import requests
import json
import threading
import random


def get_requestHeaders():
    headers = {
        # 'accept': 'application/json, text/plain, */*',
        # 'accept-encoding': 'gzip, deflate, br',
        # 'accept-language': 'zh-CN,zh;q=0.9',
        # 'content-length': '172',
        # 'content-type': 'application/json;charset=UTF-8',
        # 'dnt': '1',
        # 'origin': 'https://wallpaper.zhhainiao.com',
        # 'referer': 'https://wallpaper.zhhainiao.com/',
        # 'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-fetch-dest': 'empty',
        # 'sec-fetch-mode': 'cors',
        # 'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        # 'x-cf-device-id': 'xxxx-xxx-xxx',
        # 'x-cf-platform': 'webview'
    }
    return headers


def thd(dicts, page):
    for i in dicts:
        if i["Jpg4kUrl"] != "":
            url = i["Jpg4kUrl"]  # 存在4k就下载4k的
        elif i["Jpg1920Url"] != "":
            url = i["Jpg1920Url"]
        name = i["wname"]
        if name == '':
            # 没有文件名就随便起一个
            name = str(random.randint(1, 9)) + str(random.randint(1, 99)) + str(random.randint(1, 999999)) + ".jpg"
        print(url, name, page)
        pic = requests.get(url).content
        # 文件保存路径，我这里用到时z盘内存盘，emm，自行修改叭
        with open("z:/spider/" + name + ".jpg", 'wb') as f:
            f.write(pic)


def get_post_data(pageNumber=1, pageSize=24):
    post_data = '{"login_info":{},"cate_id":2,"tag_id":null,"sort_type":2,"page":' + str(
        pageNumber) + ',"page_size":' + str(
        pageSize) + ',"common":{"open_id":null,"token":null,"device_id":null,"player_version":0,"platform":"pc"}}'
    return post_data


if __name__ == '__main__':
    post_data = get_post_data(1, 1)
    response = requests.post("https://pcwallpaper.zhhainiao.com/wallpaper/static/list", headers=get_requestHeaders(),
                             data=post_data)
    json_data = json.loads(response.text)["data"]
    total = json_data["total"]
    print(total)
'''
    for page in range(1, 100):
        r = requests.post("https://pcwallpaper.zhhainiao.com/wallpaper/static/list",
                          headers=get_requestHeaders(),
                          data='{"login_info":{},"cate_id":2,"tag_id":null,"sort_type":2,"page":' + str(page) +
                               ',"page_size":24,'
                               '"common":{"open_id":null,"token":null,"device_id":null,"player_version":0,"platform":"pc"}}')
        json_data = r.text
        dumps = json.loads(json_data)
        dicts = dumps["data"]["list"]
        url = ""
        name = ""
        with open("json","w",encoding="utf-8") as f:
            f.write(json_data)
        threading.Thread(target=thd, args=(dicts,page,)).start()
'''
