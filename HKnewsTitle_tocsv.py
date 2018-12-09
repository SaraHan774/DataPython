# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 02:15:07 2018

@author: GAHEE HAN
"""

from urllib.request import urlopen
import bs4 
import pandas as pd

page = urlopen("http://news.hankyung.com/it")
soup = bs4.BeautifulSoup(page, "html.parser")
print(type(soup)) #<class 'bs4.BeautifulSoup'>

tags = soup.find_all("strong" , {"class":"tit"})
print(type(tags))#<class 'bs4.element.ResultSet'>
print(tags)

listags = list(tags)
print(type(listags))#<class 'list'> list로 변환해서 for문을 돌린다
print(len(listags)) #20

basket = []

for title in listags: 
    strtitle = str(title) #스트링으로 변환해서 태그를 제거한다. 
    #print(strtitle)
    #print(type(strtitle))# str으로 변환하지 않는 경우 title 은 <class 'bs4.element.Tag'>
    titlefront = strtitle.replace("<strong class=\"tit\">", "")
    SoTitleIs = titlefront.replace("</strong>", "")
    basket.append(SoTitleIs)
print(basket)       

df = pd.DataFrame(basket)
df.to_csv("HknewsTitle_IT.csv" , header = ["Issue Title"], index = True, encoding = 'ms949')

