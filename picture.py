import re
from bs4 import BeautifulSoup
import requests

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}
url="https://pic.netbian.com/4kfengjing/index.html"
r=requests.get(url,headers=headers)

r.encoding = "gbk"
html = r.text
soup = BeautifulSoup(html, "html.parser")
total_page = soup.find_all("div", class_="page")[0]
total_page=int(re.findall(r"<a.*?>(\d*)</a>",str(total_page))[-1])
imgs=soup.find_all("img",alt=True,border=False)
img_links=[]
for each in imgs:
    img_links.append("https://pic.netbian.com"+re.findall(r'src="(.*?)"',str(each))[0])

for i in range(2,total_page+1):
    url=f"https://pic.netbian.com/4kfengjing/index_{i}.html"
    r=requests.get(url,headers=headers)

    r.encoding = "gbk"
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    imgs=soup.find_all("img",alt=True,border=False)
    for each in imgs:
        img_links.append("https://pic.netbian.com"+re.findall(r'src="(.*?)"',str(each))[0])

count=0
for each in img_links:
    r=requests.get(each,headers=headers)

    name=re.findall(r"https://pic.netbian.com/uploads/allimg/(.*?).jpg",each)[0]
    print(name)
    name=re.sub(r"/","",name)+".jpg"
    print(name)
    with open(name,"wb") as f:
        f.write(r.content)
    count+=1
    if count==10:
        break