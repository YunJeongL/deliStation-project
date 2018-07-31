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



# k=[]
# file = open('file.csv','r')     # 역이름 csv파일 경로 
# csvReader = csv.reader(file)                           #-sig: utf로 인코딩했을때 처음 나오는 형식 문자 제거 
# for row in csvReader:
#     # print(row)
#     # print(len(row))
#     for r in row:
#         #print(r)
#         p = k.append(r) 
#     print(k)     
# file.close()   
        
#print(k)
#print(k[1])

k=[]
f = open('test.txt','r')
kkk = f.readlines()

f.close()
print(kkk)

# for i in k:
#     wordli = i[1:]       #상호명 빼고 워드클라우드용 형식만 추출 ["[('빵'", '15)', "('햄'", '10)', "('양상추'", '3)', "('쿠키'", '12)', "('사이다'", '7)]', '', '']


# tags2 = wordli



# print(tags2)
#tags2 = [('맛', 89), ('브런치', 63), ('분위기', 62),...]
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