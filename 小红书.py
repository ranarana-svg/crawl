url=r"https://www.xiaohongshu.com/explore?channel_id=homefeed.gaming_v3"
referer=r"https://www.xiaohongshu.com/explore?channel_id=homefeed.gaming_v3"

headers={"referer":"https://www.xiaohongshu.com/explore?channel_id=homefeed.gaming_v3",'user-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}
import requests
import re
import os
import random
if not os.path.exists(r"C:\Users\Administrator\Desktop\img"):
    os.mkdir(r"C:\Users\Administrator\Desktop\img")
resp=requests.get(url,headers=headers)
obj=re.compile("<img src=\"(?P<content>.*?)\" fetchpriority",re.S)
ret=obj.finditer(resp.text)

for con in ret:
    num=random.randint(1,111)
    
    a=con.group("content")
    img_content=requests.get(a).content
    #print(a)
    with open("C:\\Users\\Administrator\\Desktop\\img\\"+str(num)+".jpg","wb") as f:
        f.write(img_content)




                #print(resp.text)
