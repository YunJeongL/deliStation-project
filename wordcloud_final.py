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

MAIN_URL='http://www.mangoplate.com/'
driver = wd.Chrome(executable_path='.\chromedriver.exe')
driver.get(MAIN_URL)
# driver.implicitly_wait(1)
driver.find_element_by_id('main-search').send_keys('카페413프로젝트')
driver.find_element_by_class_name('btn-search').click()
driver.find_element_by_tag_name('a').click()
# 숨겨진 리뷰 끌어오기
num_of_pagedowns=20
body=driver.find_element_by_tag_name('body')
while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    try:
        driver.find_element_by_xpath("//section[@class='module review-container']/button[@class='btn-reivews-more']").click()
    except Exception as e:
        print(e)
    num_of_pagedowns-=1

reviews=[]
for i in range(1,5):
    reviews.append(driver.find_element_by_xpath("""/html/body/main/article/div[1]/div[1]/div/section[3]/ul/li[%s]/section/div[1]/div/div/span[1]"""%i).text)

# page=driver.current_url
# html=urlopen(page)
# soup=BeautifulSoup(html,"html.parser")
# GB = soup.find('section',{'class':'module review-container'})
# GB2 = GB.find_all('button',{'class':'review_fliter_item_btn'})
# a = int(GB2[0]['data-review_count'])

for i in range(6,98):
    reviews.append(driver.find_element_by_xpath("""/html/body/main/article/div[1]/div[1]/div/section[3]/ul/li[%s]/section/div[1]/div/div/span"""%i).text)
kkk = " ".join(reviews)



nlp = Twitter()
nouns = nlp.nouns(kkk)
 
count = Counter(nouns)
tags2 = count.most_common(40)
taglist = pytagcloud.make_tags(tags2, maxsize=80)
pytagcloud.create_tag_image(taglist, 'wordcloud2.jpg', size=(900, 600), fontname='Korean', rectangular=False)
    
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