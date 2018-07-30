# pip install selenium
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
file = open('C:/Users/USER/Desktop/marketName.csv','r')
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
# print(store[2])
# aa = ['카페413프로젝트', '대우부대찌개', '고갯마루집']
# bb = ['샘밭막국수 (서울본점)',	'하레', 	'보떼가젤라또', 	'교대이층집 (교대본점)',	'스시카루' ,	'탐라도야지', 	'귀족족발', 	'램하우스 (서초법원점)',	'서초장어타운', 	'명동곰돌이' ]

print(store)

a = 0               # a와 i 초기값 설정
i = 0 

driver = wd.Chrome(executable_path='C:/Users/USER/py_project/py_test/chromedriver.exe')
# 접속
driver.get(MAIN_URL)
# 망플 홈 에서 바로 키워드 입력(가게이름)
driver.find_element_by_id('main-search').send_keys(store[i])
# 검색 버튼 클릭
driver.find_element_by_class_name('btn-search').click()
# 세부 페이지 접속
driver.find_element_by_tag_name('a').click()

# 가게정보 가져오기
# 가게 리스트길이 
while a < len(store):   
                   
    # page = driver.current_url
    # html = urlopen(page)
    # time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")

    for p in soup.find('table',{'class':'info'}).tr.td:              # 가게정보 중 주소 node
        print(p)
    
    a = a+1
    i = i+1
    driver.implicitly_wait(3)
# 검색 화면에서 바로 키워드 입력(가게이름)
    driver.find_element_by_id('search').send_keys(store[i])
    driver.find_element_by_id('search').send_keys(u'\ue007')              ## hidden enter key
    driver.implicitly_wait(1)
    driver.find_element_by_tag_name('a').click()                          ## enter키 클릭


# # print(soup.prettify())                        # html 파일 전체 출력
# adress = soup.find_all('table',{'class':'info'})
# only_adress = [i.text for i in adress]
# print(only_adress)
# store[i]