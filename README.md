# SteamPY-Add-HB
批量上架HB月包里的游戏到PY<br>
需要配合仓库里的油猴插件使用<br>
标准格式如下:
```
cn 	https://store.steampowered.com/app/1088850	Marvel's Guardians of the Galaxy	FFFFF-FFFFF-FFFFF
```
![image](https://github.com/user-attachments/assets/546f2b27-e301-4ea0-ba24-2bbaaea0ab55)

复制到keys.txt里面运行dedeem.py脚本即可：<br>
其中的cookies和headers使用curl2python即可生成<br>
如果提示maybe good表示游戏激活的key与实际的游戏标题可能有出入，<br>
提示bad则代表匹歪里面有多版本需要核对。<br>
