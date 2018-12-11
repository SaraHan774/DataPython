# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:46:45 2018

@author: GAHEE HAN
"""

import urllib.request
import bs4

page = urllib.request.urlopen("https://en.wikipedia.org/wiki/Jane_Austen#List_of_wroks")
soup = bs4.BeautifulSoup(page, "html.parser")
tags = soup.find("div", {"class" : "div-col columns column-width"})

basket = []

for book in tags.findAll("li"):
    strbook = book.strings
    libook = list(strbook)
    basket.append(libook)
print(basket)
    
import pandas as pd
df = pd.DataFrame(basket)
df.to_csv("jane.csv")
df.to_excel("jane.xlsx")
with open("jane.txt", "w", encoding = "utf-8") as file:
    file.write(str(basket))
    
import matplotlib.pyplot as plt 
#import matplotlib
import pytagcloud

def wordcount(word):
    return word[0]

janelist = pd.read_excel("jane.xlsx", names = ('title', 'year', 'n3', 'n4', 'n5'))
print(janelist)

janeaxis = janelist.drop(['year', 'n3', 'n4', 'n5'], axis = 1)
#열 삭제를 위해서는 axis = 1을 명시해야 열 삭제라는 것이 명시된다. 
janelist = janeaxis.drop([0][:])
janelist['li'] = range(1 , len(janelist['title'])+1, 1)
#알파벳 카운트를 위한 열 추가하기 
janelist.to_excel("janelist.xlsx") 
print(janelist) 

data = janelist.set_index('title').groupby(wordcount).count()["li"]

print(type(data)) #<class 'pandas.core.series.Series'>

data.plot()
plt.show()
data.plot(kind = "bar")
plt.show()
data.plot.pie()
plt.show()

#워드클라우드 만들기
taglist = pytagcloud.make_tags(dict(data).items(), maxsize = 80)
#data는 딕셔너리가 아니기 떄문에 반드시 dict()로 형 변환 필요 
pytagcloud.create_tag_image(taglist, "text3.jpg", size = (640,480), fontname = 'Nobile', rectangular = True)




