# pip install selenium
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

def review(m_name):
    MAIN_URL='http://www.mangoplate.com/'
    driver = wd.Chrome(executable_path='.\chromedriver.exe')
    driver.get(MAIN_URL)
    # driver.implicitly_wait(1)
    driver.find_element_by_id('main-search').send_keys(m_name)
    driver.find_element_by_class_name('btn-search').click()
    driver.find_element_by_tag_name('a').click()
    # 숨겨진 리뷰 끌어오기
    num_of_pagedowns=50
    body=driver.find_element_by_tag_name('body')
    while num_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        try:
            driver.find_element_by_xpath("//section[@class='module review-container']/button[@class='btn-reivews-more']").click()
        except Exception as e:
            print(e)
        num_of_pagedowns-=1

    reviews=[]
    for i in range(1,5):
        reviews.append(driver.find_element_by_xpath("""/html/body/main/article/div[1]/div[1]/div/section[3]/ul/li[%s]/section/div[1]/div/div/span[1]"""%i).text)

    page=driver.current_url
    html=urlopen(page)
    soup=BeautifulSoup(html,"html.parser")
    GB = soup.find('section',{'class':'module review-container'})
    GB2 = GB.find_all('button',{'class':'review_fliter_item_btn'})
    a = int(GB2[0]['data-review_count'])

    for i in range(6,a):
        reviews.append(driver.find_element_by_xpath("""/html/body/main/article/div[1]/div[1]/div/section[3]/ul/li[%s]/section/div[1]/div/div/span"""%i).text) 
    
    return(reviews)

# 영어, 특정 문자 제거
def clean_text(reviews):
    cleaned_text = re.sub('[a-zA-Z]' , '', reviews)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]','', cleaned_text)
    return cleaned_text
    
# 워드클라우드
def wordcloud(cleaned_text):
    count = Counter(cleaned_text) #추출된 명사로 빈도 계산 
    wordInfo = dict()

    for tags,counts in count.most_common(30):
        wordInfo[tags] = counts

    taglist = pytagcloud.make_tags(dict(wordInfo).items(), maxsize=80)
    pytagcloud.create_tag_image(taglist,'test1.jpg', size=(640,480),  fontname='Nanum Gothic Coding', rectangular=False)
