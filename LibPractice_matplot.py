# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:15:34 2018

@author: GAHEE HAN
"""

import json
import re
import pandas as pd
from konlpy.tag import Twitter
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
import pytagcloud
import codecs
import webbrowser

openFileName = 'crtest.json'
cloudImagePath = openFileName + '.jpg'  #왜 json 뒤에 jpg형식을 붙인거지? 
rfile = codecs.open(openFileName, 'r', encoding = 'utf-8').read()
jsonData = json.loads(rfile)
message = ''
for item in jsonData:
    if 'message' in item.keys():#re.sub(pattern, repl, string) string에서 pattern과 매치하는 텍스트를 repl로 치환한다
        #The "\w" means "any word character" which usually means alphanumeric (letters, numbers, regardless of case) plus underscore (_)
        message = message + re.sub(r'[^\w]', ' ', item['message']) + ' '
nlp = Twitter()
nouns = nlp.nouns(message)
count = Counter(nouns) #Counter() - 시퀀스 타입 요소 개수 세기 
wordInfo = { }
for tags, counts in count.most_common(50): #tag 의 개수가 counts 개 나오는 것 확인
    if (len(str(tags)) > 1): #태그를 스트링으로 변환, 길이를 확인 - 한 글자 이상이면 
        wordInfo[tags] = counts #wordInfo 딕셔너리에 태그 : 개수 의 형식으로 삽입한다. 
        print ("%s : %d" % (tags, counts)) #프린트는 스트링 : 숫자 형식으로
print(type(wordInfo)) #wordInfod의 타입은 딕셔너리 
print(wordInfo)

wordInfo2={'빈도수':wordInfo} #wordInfo가 빈도수를 나타내는 딕셔너리임 명시 

font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
                                #fname  = font_location, size = 숫자 지정도 가능
matplotlib.rc('font', family=font_name) #family = 왜 지정하는 건지 모르겠음 
dfdata = pd.DataFrame(wordInfo, index=[0]) #pandas로 DataFrame 형성, wordInfo의 내용을 1행의 DF으로 만든다 
# 단어가 한줄로 나열되어서 컨솔에 찍힘
print(dfdata)

dfdata.plot(kind='bar') #‘bar’ : vertical bar plot - 이것 말고도 kind = 'str'에 들어갈 수 있는 키워드 많아

plt.xlabel('주요 단어') #matplotlib.pyplot 을 plt로 임포트 한 것 
plt.ylabel('빈도수')
plt.show() #show명령은 시각화 명령을 실제로 차트로 렌더링하고 마우스 움직임 등의 이벤트를 기다리라는 지시 
#주피터 노트북에서는 셀 단위로 플롯 명령을 자동 렌더링해주므로 show필요 없는데, 일반 파이썬 인터프리터의 경우 마지막에 실행 


dfdata2=pd.DataFrame(wordInfo2) #빈도수 :{태그이름 : 개수} 를 표현한 딕셔너리 
print(dfdata2) #1행은 빈도수, 2행부터 그 아래로 wordInfo 의 내용이 두 열로 출력됨 

dfdata2.plot(kind='bar')#인덱스는 자동으로 x 축이 된다. 
plt.show()#plt.show()와 plt.savefig() 둘 중 하나만 실행해야 한다. 둘다 하면 저장은 되지 않는다 
plt.savefig("dfdata2bar.jpg", bbox_inches='tight')
dfdata2.plot.pie(subplots=True)
plt.show()
plt.savefig("dfdata2pie.jpg", bbox_inches='tight') #저장하는 형식, Bbox in inches. Only the given portion of the figure is saved. 
#If 'tight', try to figure out the tight bbox of the figure. If None, use savefig.bbox

taglist = pytagcloud.make_tags(dict(wordInfo).items(), maxsize=80) #tags = make_tags(get_tag_counts(YOUR_TEXT), maxsize=120)
pytagcloud.create_tag_image(taglist, cloudImagePath, size=(640, 480), fontname='korean',
rectangular=True) #cloudImagePath = openFileName + '.jpg' 이라고 위에서 선언함

#create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')
webbrowser.open(cloudImagePath)#웹브라우저로 열기
