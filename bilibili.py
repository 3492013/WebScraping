import re
from bs4 import BeautifulSoup
import requests
import json
import os

bid="BV1sh411X7Af"
url="https://www.bilibili.com/video/"+bid
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
         "Referer":url,
         }
r=requests.get(url,headers=headers)

r.encoding="utf-8"
html=r.text
soup=BeautifulSoup(html,"html.parser")
head=soup.find_all("head")[0]
playinfo=re.findall(r"playinfo__=(.*?)</script>",str(head))[0]
playinfo=json.loads(playinfo)
video_url=playinfo["data"]["dash"]["video"][0]["baseUrl"]
audio_url=playinfo["data"]["dash"]["audio"][0]["baseUrl"]

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

audio_content=requests.get(audio_url,headers=headers)
received_audio=0
try:
    os.remove("bilibili.mp3")
except:
    pass
with open("bilibili.mp3","ab") as f:
    while int(audio_content.headers["Content-Length"])>received_audio:
        headers["Range"]="bytes"+str(received_audio)
        r=requests.get(audio_url,headers=headers)
        f.write(r.content)
        received_audio+=len(r.content)

'''
合并用ffmpeg
'''