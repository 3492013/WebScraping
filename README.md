# 正则表达式

| 操作符 |         说明         |
| :----: | :------------------: |
|  [ab]  |       字符范围       |
| [^ab]  |     排除字符范围     |
|   .    | 单个字符不包括换行符 |
|   *    |     重复0或多次      |
|   +    |     重复1或多次      |
|   ?    |      重复0或1次      |
|   \|   |          或          |
|  {m}   |       重复m次        |
| {m,n}  |      重复m到n次      |
|  ^abc  |    字符串开头abc     |
|  abc$  |    字符串结尾abc     |
|   \d   |         数字         |
|   \w   |     [A-Za-z0-9_]     |

```python
import re
.*#贪婪
.*?#非贪婪
re.S#.匹配换行符
re.findall(r"","")#返回list
re.findall(r"()","")#只保留括号里的内容
re.sub(r"a","A","")#用A替换a
```

# 请求网页

## get

```python
import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}
r=requests.get('http://placekitten.com/200/300',headers=headers)
```

## post

```python
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}
data={}
data['i']='你好'
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTION'
r=requests.post(url,headers=headers,data=data)
```

# 网页处理

```python
from bs4 import BeautifulSoup
import json
r.encoding="utf-8"
html=r.text
soup=BeautifulSoup(html,"html.parser")
a_list=soup.find_all("a")
a_list=soup.find_all(id="head")
a_list=soup.find_all(class_=True)
a_list=soup.find_all(text="hao123")
a_list=soup.find_all("span",class_="title")
head=soup.find_all("head")[0]
playinfo=re.findall(r"playinfo__=(.*?)</script>",str(head))[0]
playinfo=json.loads(playinfo)
video_url=playinfo["data"]["dash"]["video"][0]["baseUrl"]
audio_url=playinfo["data"]["dash"]["audio"][0]["baseUrl"]
```

## get

```python
#文本
with open("douban.txt",'a',encoding='utf-8')as f:
    for each in result:
        f.write(each)
#图片
with open('cat.jpg','wb') as f:
    f.write(r.content)
#视频
video_content=requests.get(video_url,headers=headers)
received_video=0
try:
    os.remove("bilibili.mp4")
except:
    pass
with open("bilibili.mp4","ab") as f:
    while int(video_content.headers["Content-Length"])>received_video:
        headers["Range"]="bytes"+str(received_video)
        r=requests.get(video_url,headers=headers)
        f.write(r.content)
        received_video+=len(r.content)
```

## post

```python
#字典
target=r.json()['translateResult'][0][0]['tgt']
```
