from DrissionPage import*
from wordcloud import*
#from matplotlib.pyplot import*
from matplotlib import pyplot
import re
texts = ''
ergou = ChromiumPage()
ergou.listen.start('comment/list')
url =
ergou.get(url)
ele1 = ergou.ele("css:.jp8u3iov")
ele1.click()

for i in range(1,31):
    result = ergou.listen.wait()
    JSON = result.response.body()
    print(result)
    print(JSON)
    #ergou.wait(1)
     #   els2 = ergou.ele('加载中')
      #  ergou.scroll.to_see(ele2)
    COMMENTLIST = JSON['comments']
    for comment in COMMENTLIST:
        nickname = comment['user']['nickname']
        ip = comment['ip-lable']
        text = comment['text']
        texts += text
        print(f'来自{ip}的【{nickname}】说： {text}')
        ele2 = ergou.ele('加载中')
        ergou.scroll.to_see(ele2)
open('uuigj.txt','w', encoding = 'utf-8').write(texts)
texts = open('uuigj.txt','r', encoding = 'utf-8').read()

texts = re.sub('\[.*?\]', '' , texts)

wc = WordClouc(font_path = '111.txt', width = '1920', height = '1080', background_color = 'write').generate(texts)
matplotlib.pyplot.imshow(wc)
matplotlib.pyplot.show()