#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import json
import re

html = '''<div class="herald box aside reviews" data-topics="article112704 reviews novels">
    <div class="category-line reviews"></div>
    <div class="thumbnail" style="background-image: url(/thumbnails/cover400x200/encyc/A19213-2600108680.1487776406.jpg); background-position: 52.000% 1.970%;">
      <div class="overlay">
        <div class="category reviews">
          review
        </div>
        <div class="comments"><a href="/cms/discuss/112704">14 comments</a></div>
      </div>
      <a href="/review/my-big-sister-lives-in-a-fantasy-world/novel-1/.112704" data-track="id=39363&amp;from=HP.A"></a>
    </div>
    <div class="wrap">
      <div>
        <h3>
          <a href="/review/my-big-sister-lives-in-a-fantasy-world/novel-1/.112704" data-track="id=39363&amp;from=HP.A">My Big Sister Lives in a Fantasy World Novel 1</a>
        </h3>
        <div class="byline">
          <time datetime="2017-02-26T15:00:00Z">
            Feb 26, 23:00
          </time>
          <div class="comments"><a href="/cms/discuss/112704">14 comments</a></div>
          <span class="topics">
            <span class="novels">novels</span>
          </span>
        </div>
        <div class="preview">
          <span class="intro">This wide-ranging parody of <em>chuunibyou</em> tropes pushes the envelope in some eyebrow-raising ways, but it's still bound to offer otaku fans a fun read.</span>
          <span class="full">― Whether you have a weird sibling or are the weird sibling, families often have dynamics that can feel odd to an outside perspective. In the case of Yuichi Sakaki's family in My Big Sister Lives in a Fantasy World, his older sister Mutsuko suffers from ...</span>
        </div>
      </div>
    </div>
  </div>'''

htmlurl= open('Netnews.html').read()
soup = BeautifulSoup(htmlurl,"html.parser")
trs = soup.findAll('div',{'class':"herald"})
length = len(trs)
jsondatas = []
arr={}
for i in range(length):
    title=trs[i].h3.text
    datetime=trs[i].time.text
    intro=trs[i].findAll('span',{'class':"intro"})[0].text
    img=trs[i].findAll('div',{'class':"thumbnail"})[0].attrs['style']
    tag=trs[i].findAll('span',{'class':"topics"})[0].text
    arr={'Title':title,'Img':img,'Intro':intro,'Tag':tag,'Time':datetime}
    jsondatas.append(json.dumps(arr,ensure_ascii=False))
print jsondatas

