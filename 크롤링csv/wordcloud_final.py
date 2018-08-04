# -*- coding:utf-8 -*-
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import itemgetter
import sys
import glob
import os
import time
from collections import Counter
import pytagcloud
import re
from lxml import html
import pytagcloud # requires Korean font support
import urllib.request, urllib.parse, urllib.error
import random
import webbrowser
from konlpy.tag import Twitter
import csv

MAIN_URL='http://www.mangoplate.com/'
driver = wd.Chrome(executable_path='.\chromedriver.exe')
driver.get(MAIN_URL)

k = []
station = []
file = open('subwayInfo1.csv','r')     # 역이름 csv파일 경로 
csvReader = csv.reader(file)                           #-sig: utf로 인코딩했을때 처음 나오는 형식 문자 제거 
for row in csvReader:
    k.append(row)    
file.close()            


for i in k:                                                 # 이중 문자열 1개의 문자열로 만들기
    for j in i:
        # print(j)
        j = ''.join(j.split())                              #리스트의 단어 안의 공백 제거
        station.append(j)                                   #station=[역삼역, 합정역']

for st in station:
    driver.find_element_by_id('main-search').send_keys('%s역' % (st))
    driver.find_element_by_class_name('btn-search').click()

    for i in range(1,6):
        for j in range(1,3):
            # driver.implicitly_wait(1)
            m_name=driver.find_element_by_xpath('/html/body/main/article/div[2]/div/div/section/div[2]/ul/li[%s]/div[%s]/figure/figcaption/div/a/h2'% (i,j))
            m_name=m_name.text
            #print(m_name)
            #세부페이지 들어감
            driver.find_element_by_xpath('/html/body/main/article/div[2]/div/div/section/div[2]/ul/li[%s]/div[%s]/figure/figcaption/div/a/h2'% (i,j)).click()
            # 숨겨진 리뷰 끌어오기
            
            num_of_pagedowns=10
            body=driver.find_element_by_tag_name('body')
            while num_of_pagedowns:
                body.send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
                try:
                    driver.find_element_by_xpath("//section[@class='module review-container']/button[@class='btn-reivews-more']").click()
                except:
                    pass
                num_of_pagedowns-=1

            reviews=[]
            for n in range(1,5):
                try:
                    reviews.append(driver.find_element_by_xpath("""/html/body/main/article/div[1]/div[1]/div/section[3]/ul/li[%s]/section/div[1]/div/div/span[1]"""%n).text)
                except:
                    pass
            # page=driver.current_url
            # html=urlopen(page)
            # soup=BeautifulSoup(html,"html.parser")
            # GB = soup.find('section',{'class':'module review-container'})
            # GB2 = GB.find_all('button',{'class':'review_fliter_item_btn'})
            # a = int(GB2[0]['data-review_count'])

            for n in range(6,98):
                try:
                    reviews.append(driver.find_element_by_xpath("""/html/body/main/article/div[1]/div[1]/div/section[3]/ul/li[%s]/section/div[1]/div/div/span"""%n).text)
                except:
                    pass
            totalreviews = " ".join(reviews)  

            nlp = Twitter()
            nouns = nlp.nouns(totalreviews)

            count = Counter(nouns)
            tags2 = count.most_common(50)   #tags2 = [('맛', 89), ('브런치', 63), ('분위기', 62),...]
            #print(tags2)
            # alldata={}
            # alldata[m_name] = tags2
            alldata = [m_name, tags2]
            print(alldata)    
            
            # output_file=sys.argv[1]
            # filewriter=open('wordList.csv', 'w','a') #append
            # filewriter.write(str(alldata)+'\n')
            # filewriter.close()
            # print('Output')

            with open('wordList.csv', 'a') as f:  # Just use 'w' mode in 3.x #딕셔너리 ziip csv파일로 만들기
                f.write(str(alldata)+'\n')
                f.close()
                print('Output')

            driver.back()

    driver.find_element_by_xpath('/html/body/header/a/img[1]').click()

# 새로운 역 검색을 위한 메인 페이지 이동

# taglist = pytagcloud.make_tags(tags2, maxsize=50)
# pytagcloud.create_tag_image(taglist, 'wordcloud2.jpg', size=(300, 300), fontname='SSangMun', rectangular=False)
    
##########################################################################################



# output_file=sys.argv[1]
# filewriter=open(output_file,'a') #append
# for i in range(max_index):
#     filewriter.write(str(reviews[i])+'\n')
# filewriter.close()
# print('Output')

# first_url='http://wordcloud.kr/'
# driver = wd.Chrome(executable_path='.\chromedriver.exe')
# driver.get(first_url)

# driver.find_element_by_id('text').send_keys(reviews)
# driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/form/div[8]/button[1]").click()
# time.sleep(6)
# driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/form/div[8]/button[2]").click()
# time.sleep(1)
# driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/form/button/span").click()