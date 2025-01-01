# -*- coding: utf-8 -*-
import urllib.parse
import requests
import urllib
import time

#这两个部分需要自己生成
cookies = {

}

headers = {

}

def addgame(id,key,price,region):

    data = {
        'gameId': id,
        'keys': key,
        'keyWord': '',
        'sellPrice': price,
        'syncUs': '0' if region=='cn' else '1',
    }

    response = requests.post('https://steampy.com/xboot/steamKeySale/startSell', cookies=cookies, headers=headers, data=data)
    print(response.json().get("message"))
    time.sleep(10)

f=open("keys.txt", mode="r", encoding="utf-8")
games_line=f.readlines()
f.close()
for game_line in games_line:
    found=0
    if "请求失败" in game_line:  #删除无key行
        continue
    region,url,name,key=game_line.split("\t")
    encodeurl=urllib.parse.quote(url)
    response = requests.get(f'https://steampy.com/xboot/steamGame/saleKeyByUrl?pageNumber=1&pageSize=10&sort=id&order=asc&gameUrl={encodeurl}&gameName=',
    cookies=cookies,
    headers=headers,
)
    if len(response.json().get("result").get("content"))==1:  #返回列表只有一个游戏，可能匹配，按最低价上架游戏并人工提示
        print(name,key,response.json().get("result").get("content")[0].get("gameName"),"maybegood")
        addgame(response.json().get("result").get("content")[0].get('id'),key,response.json().get("result").get("content")[0].get('keyPrice'),region)
        continue
    for gamelist in response.json().get("result").get("content"):
        if gamelist.get("gameName")== name:
            print(name,key,"good")
            addgame(gamelist.get('id'),key,gamelist.get('keyPrice'),region)
            found=1   #从返回列表里面找到匹配游戏则退出循环，按最低价上架游戏
            break
    if found==0:
        print(region,url,name,key,"bad")#没有匹配游戏则提示

