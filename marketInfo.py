from selenium import webdriver as wd
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import itemgetter
import sys
import glob
import os
import csv


# 기본 접속 사이트
MAIN_URL='http://www.mangoplate.com/'
# 브라우저 띄우기

k = []
store = []
file = open('marketName.csv','r')
csvReader = csv.reader(file)
for row in csvReader:
    k.append(row)    
file.close()                    

for i in k:                     # 이중 문자열 1개의 문자열로 만들기
    for j in i:
        # print(j)
        store.append(j)    

while True:                     # store 리스트 중 공백 문자열 제거
    try:
        store.remove("")
    except ValueError:
        break        


driver = wd.Chrome(executable_path='C:\Users\student\Dev\work\chromedriver.exe')
# 접속
driver.get(MAIN_URL)
# 망플 홈 에서 바로 키워드 입력(가게이름)
for i in store:
    driver.find_element_by_id('main-search').send_keys(i)
    # 검색 버튼 클릭
    driver.find_element_by_class_name('btn-search').click()
    # 세부 페이지 접속
    for i in range(1,6):
        for j in range(1,3):
            driver.find_element_by_xpath('/html/body/main/article/div[2]/div/div/section/div[2]/ul/li[%s]/div[%s]/figure/figcaption/div/a/h2'% (i,j)).click()
            html = driver.page_source
            soup = BeautifulSoup(html,"html.parser")
            address=soup.find('table',{'class':'info'}).tr.td              # 가게정보 중 주소 node
            print(address)

            driver.back()
    driver.find_element_by_xpath('/html/body/header/a/img[1]').click()

