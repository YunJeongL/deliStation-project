# -*- coding:utf-8 -*-
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import os
import re
import random
import webbrowser
import time
import pandas as pd
import pymysql as my
import csv


# def crawling(subway_name):

MAIN_URL='http://www.mangoplate.com/'
driver = wd.Chrome('/Users/kimchaeyeon/py_project/py_test/chromedriver.exe')
driver.get(MAIN_URL)
# driver.implicitly_wait(1)
data1 = pd.read_csv('subwayInfo.csv')
for name in data1['전철역명']:
    driver.find_element_by_id('main-search').send_keys(name+'역')
    driver.find_element_by_class_name('btn-search').click()
     
    data=[]

    for i in range(1,6):
        for j in range(1,3):
            
            # 가게이름
            m_name=driver.find_element_by_xpath('/html/body/main/article/div[2]/div/div/section/div[2]/ul/li[%s]/div[%s]/figure/figcaption/div/a/h2'% (i,j))
            m_name=m_name.text
            #print(m_name)
            # 세부페이지 들어감
            driver.find_element_by_xpath('/html/body/main/article/div[2]/div/div/section/div[2]/ul/li[%s]/div[%s]/figure/figcaption/div/a/h2'% (i,j)).click()
            # 가게정보
            
            # 평점
            rating=driver.find_element_by_xpath('/html/body/main/article/div[1]/div[1]/div/section[1]/header/div[1]/span/strong/span')
            rating=rating.text
            #print(rating)
            # 호불호
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            GB = soup.find('section',{'class':'module review-container'})
            GB2 = GB.find_all('button',{'class':'review_fliter_item_btn'})
            tasteGood = GB2[1]['data-review_count']
            tasteSoso = GB2[2]['data-review_count']
            tasteBad = GB2[3]['data-review_count']
            taste = (int(tasteSoso)+int(tasteBad))/int(tasteGood)
            # 리뷰
            # num_of_pagedowns=20
            # body=driver.find_element_by_tag_name('body')
            # while num_of_pagedowns:
            #     body.send_keys(Keys.PAGE_DOWN)
            #     time.sleep(1)
            #     try:
            #         driver.find_element_by_xpath("//section[@class='module review-container']/button[@class='btn-reivews-more']").click()
            #     except Exception as e:
            #         print(e)
            #     num_of_pagedowns-=1

            # reviews=[]
            # for i in range(1,5):
            #     reviews.append(driver.find_element_by_xpath("""/html/body/main/article/div[1]/div[1]/div/section[3]/ul/li[%s]/section/div[1]/div/div/span[1]"""%i).text)

            # for i in range(6,98):
            #     reviews.append(driver.find_element_by_xpath("""/html/body/main/article/div[1]/div[1]/div/section[3]/ul/li[%s]/section/div[1]/div/div/span"""%i).text)
            # kkk = " ".join(reviews)
            # nlp = Twitter()
            # nouns = nlp.nouns(kkk)  
            # count = Counter(nouns)
            # tags2 = count.most_common(50)

            # 2차원 리스트 생성(가게명,역,평점, 호불호, 리뷰)
            all_data=[m_name,name,rating, taste]
            data.append(all_data)
            print(data)
            # 뒤로가기
            driver.back()

    # 새로운 역 검색을 위한 메인 페이지 이동
    driver.find_element_by_xpath('/html/body/header/a/img[1]').click()