import re
from bs4 import BeautifulSoup
import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}
for i in range(0,10):
    r=requests.get('https://movie.douban.com/top250?start='+str(i*25),headers=headers)

    r.encoding="utf-8"
    html=r.text
    soup=BeautifulSoup(html,"html.parser")
    title_list=soup.find_all("div",class_="hd")
    titles=[]
    for each in title_list:
        titles.append(re.findall(r'<span class="title">(.*)</span>',str(each))[0])
    for each in titles:
        print(each)