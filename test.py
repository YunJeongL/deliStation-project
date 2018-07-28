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

def crawling(subway_name):
    
    MAIN_URL='http://www.mangoplate.com/'
    driver = wd.Chrome(executable_path='.\chromedriver.exe')
    driver.get(MAIN_URL)
    # driver.implicitly_wait(1)
    driver.find_element_by_id('main-search').send_keys(subway_name)
    driver.find_element_by_class_name('btn-search').click()

    data=[]
    for i in range(1,5):
        for j in range(1,2):
            #가게이름
            m_name=driver.find_element_by_xpath('/html/body/main/article/div[2]/div/div/section/div[2]/ul/li[%s]/div[%s]/figure/figcaption/div/a/h2'% (i,j).text)
            print(m_name)
            #세부페이지 들어감
            driver.find_element_by_xpath('/html/body/main/article/div[2]/div/div/section/div[2]/ul/li[%s]/div[%s]/figure/a/div/img'% (i,j)).click()
            #가게정보
            

            #호불호
            good=driver.find_element_by_xpath('/html/body/main/article/div[1]/div[1]/div/section[3]/div/ul/li[1]/button')
            soso=driver.find_element_by_xpath('/html/body/main/article/div[1]/div[1]/div/section[3]/div/ul/li[2]/button')
            bad=driver.find_element_by_xpath('/html/body/main/article/div[1]/div[1]/div/section[3]/div/ul/li[3]/button')

            print(bad)
            #리뷰
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

            for i in range(6,98):
                reviews.append(driver.find_element_by_xpath("""/html/body/main/article/div[1]/div[1]/div/section[3]/ul/li[%s]/section/div[1]/div/div/span"""%i).text)
            kkk = " ".join(reviews)
            nlp = Twitter()
            nouns = nlp.nouns(kkk)  
            count = Counter(nouns)
            tags2 = count.most_common(50)

            # 2차원 리스트 생성(가게명, 호불호, 리뷰)
            all_data=[subway_name,m_name, good, soso, bad, kkk]
            data.append(all_data)
            # 뒤로가기
            driver.back()
    # 새로운 역 검색을 위한 메인 페이지 이동
    driver.find_element_by_class_name('mp_logo_img mp_logo_img_orange').click()