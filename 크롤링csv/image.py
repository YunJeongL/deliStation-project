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
stores = []
file = open('sto.csv','r')     # 역이름 csv파일 경로 
csvReader = csv.reader(file)                           #-sig: utf로 인코딩했을때 처음 나오는 형식 문자 제거 
for row in csvReader:
    k.append(row)    
file.close()            
#print(k)

for i in k:                                                 # 이중 문자열 1개의 문자열로 만들기
    for j in i:
        # print(j)
        j = ''.join(j.split())                              #리스트의 단어 안의 공백 제거
        stores.append(j)                                   #station=[역삼역, 합정역']

for st in stores:
    
    driver.find_element_by_id('main-search').send_keys('%s' % (st))
    driver.find_element_by_class_name('btn-search').click()

        # driver.implicitly_wait(1)
        # m_name=driver.find_element_by_xpath('/html/body/main/article/div[2]/div/div/section/div[2]/ul/li[%s]/div[%s]/figure/figcaption/div/a/h2'% (i,j))
        # m_name=m_name.text

        #세부페이지 들어감
    path =driver.find_element_by_xpath('/html/body/main/article/div[2]/div/div/section/div[2]/ul/li[1]/div/figure/a/div/img')
    #                              /html/body/main/article/div[2]/div/div/section/div[2]/ul/li[1]/div[2]/figure/a/div/img
    #                              /html/body/main/article/div[2]/div/div/section/div[2]/ul/li[1]/div[1]/figure/figcaption/div/a/h2
    #                               /html/body/main/article/div[2]/div/div/section/div[2]/ul/li[1]/div/figure/a/div/img
    
    links = path.get_attribute('src')
    get = [st, links]
    
    with open('images.csv', 'a', encoding='utf-8') as f:  # Just use 'w' mode in 3.x #딕셔너리 ziip csv파일로 만들기
        f.write(str(get)+'\n')
        f.close()
        print('Output')
    # kaka = '하'
    driver.find_element_by_xpath('/html/body/header/a/img[1]').click()

    # # 숨겨진 리뷰 끌어오기
    # body = driver.find_element_by_tag_name('body')
    # num_of_pagedowns=1
    # while num_of_pagedowns:
    #     body.send_keys(Keys.PAGE_DOWN)
    #     #time.sleep(0.5)
    #     try:
    #         driver.find_element_by_xpath("//section[@class='module review-container']/button[@class='btn-reivews-more']").click()
    #     except:
    #         pass
    #     num_of_pagedowns-=1

    # reviews=[]
    # for n in range(1,5):
    #     try:
    #         reviews.append(driver.find_element_by_xpath("""/html/body/main/article/div[1]/div[1]/div/section[3]/ul/li[%s]/section/div[1]/div/div/span[1]"""%n).text)
    #     except:
    #         pass
    # # page=driver.current_url
    # # html=urlopen(page)
    # # soup=BeautifulSoup(html,"html.parser")
    # # GB = soup.find('section',{'class':'module review-container'})
    # # GB2 = GB.find_all('button',{'class':'review_fliter_item_btn'})
    # # a = int(GB2[0]['data-review_count'])

    # for n in range(6,98):
    #     try:
    #         reviews.append(driver.find_element_by_xpath("""/html/body/main/article/div[1]/div[1]/div/section[3]/ul/li[%s]/section/div[1]/div/div/span"""%n).text)
    #     except:
    #         pass
    # totalreviews = " ".join(reviews)  

    # nlp = Twitter()
    # nouns = nlp.nouns(totalreviews)

    # count = Counter(nouns)
    # tags2 = count.most_common(20)   #tags2 = [('맛', 89), ('브런치', 63), ('분위기', 62),...]
    # #print(tags2)
    # # alldata={}
    # # alldata[m_name] = tags2

    # #print(alldata)    


    # taglist = pytagcloud.make_tags(tags2, maxsize=50)
    # words = []
    # for g in taglist:
    #     words.append(g['tag'])
    # listt = [st,words[:6]]
        
    #print(taglist)

        # pytagcloud.create_tag_image(taglist, 'home%s.jpg'%(kaka), size=(500, 500), fontname='Korean', rectangular=False)

                                        



# 새로운 역 검색을 위한 메인 페이지 이동


    
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