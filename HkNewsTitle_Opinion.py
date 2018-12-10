# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:09:56 2018

@author: GAHEE HAN
"""

import urllib.request
import bs4 
import pandas as pd

openpage = urllib.request.urlopen("http://news.hankyung.com/tag/biz%EC%B9%BC%EB%9F%BC?page=1")
print(type(openpage)) #<class 'http.client.HTTPResponse'>
soup = bs4.BeautifulSoup(openpage, "html.parser")
print(type(soup)) #<class 'bs4.BeautifulSoup'>
souptext = soup.get_text
#print(souptext)
print(type(souptext))#<class 'method'>
tags = soup.find_all("strong" , {"class" : "tit"})
conts = soup.find_all("p", {"class" : "read"})

#print(type(tags)) #<class 'bs4.element.ResultSet'>
#print(tags)

listtags = list(tags)
listconts = list(conts)

basket = []
for title in listtags:
    strtitle = str(title)
    strtitle = strtitle.replace("<strong class=\"tit\">", "")
    strtitle_is = strtitle.replace("</strong>", "") 
    basket.append(strtitle_is)
#print(basket)
basketcont = [] 
for content in listconts:
    strconts = str(content)
    strconts = strconts.replace("<p class=\"read\">", "")
    strconts_is = strconts.replace("</p>", "")
    basketcont.append(strconts_is)
#    print(basketcont)
basketall = [] 
for i in range(0,20):
    basketall.append(basket[i])
    basketall.append(basketcont[i])
print(basketall)

df = pd.DataFrame(basketall)
df_csv = df.to_csv("HkNewsTitleAndConts_Opinion.csv", header = ["Opinion Biz"], index = False, encoding = 'ms949' )