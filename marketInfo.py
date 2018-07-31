from selenium import webdriver
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
file = open('subwayInfo.csv','r', encoding='UTF8')
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
print(store)

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
# 접속
driver.get(MAIN_URL)


for m in store:
    driver.find_element_by_id('main-search').send_keys('%s' % m)
    # 검색 버튼 클릭
    driver.find_element_by_class_name('btn-search').click()
    # 세부 페이지 접속
    for i in range(1,6):
        for j in range(1,3):
            driver.find_element_by_xpath('/html/body/main/article/div[2]/div/div/section/div[2]/ul/li[%s]/div[%s]/figure/figcaption/div/a/h2'% (i,j)).click()
                # 가게이름
            name=driver.find_element_by_xpath('/html/body/main/article/div[1]/div[1]/div/section[1]/header/div[1]/span/h1').text
                # 주소
            try:
                address=driver.find_element_by_xpath('/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[1]/td').text
            except: address='None'
            # 전화번호
            try:
                phone=driver.find_element_by_xpath('/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[2]/td').text
            except: phone='None'
            # 음식종류
            try:
                food=driver.find_element_by_xpath('/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[3]/td').text
            except: food='None'
            # 가격대
            try:
                price=driver.find_element_by_xpath('/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[4]/td').text
            except: price='None'
            # 주차
            try:
                parking=driver.find_element_by_xpath('/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[5]/td').text
            except: parking='None'
            # 영업시간
            try:
                time=driver.find_element_by_xpath('/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[6]/td').text
            except: time='None'

            all_data=[name,address,phone,food,price,parking,time]
            print(all_data)
            output_file=sys.argv[1]
            filewriter=open(output_file,'a') #append
            filewriter.write(str(all_data)+'\n')
            filewriter.close()
            print('Output')
            driver.back()
    driver.find_element_by_xpath('/html/body/header/a/img[1]').click()

