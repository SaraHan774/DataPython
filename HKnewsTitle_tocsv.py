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
    strtitle = str(title) #스트링으로 변환해서 태그를 제거한다
    #print(type(strtitle))# str으로 변환하지 않는 경우 title 은 <class 'bs4.element.Tag'>
    titlefront = strtitle.replace("<strong class=\"tit\">", "") #앞의 태그를 제거한다
    SoTitleIs = titlefront.replace("</strong>", "") #뒤의 태그를 제거한 것이 최종 Title 문자열이다
    basket.append(SoTitleIs) #빈 리스트에 만든 문자열을 append 한다 
print(basket) #리스트를 출력한다. 

df = pd.DataFrame(basket) #pandas DataFrame을 이용해서
df.to_csv("HknewsTitle_IT.csv" , header = ["Issue Title"], index = True, encoding = 'ms949') #to_csv메소드를 이용해 엑셀 저장 
#encoding = 'utf-8'로 저장하면 엑셀 파일로 열었을 때 한글 깨짐 -> encoding = 'ms949'로 바꾸면 깨짐 현상 해결

