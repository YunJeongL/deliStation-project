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



MAIN_URL='http://www.mangoplate.com/'

k = []
store = []
file = open('C:/Users/USER/Desktop/marketName.csv','r')     # 가게이름 csv파일 경로
csvReader = csv.reader(file)
for row in csvReader:
    k.append(row)    
file.close()                    

for i in k:                                                 # 이중 문자열 1개의 문자열로 만들기
    for j in i:
        # print(j)
        store.append(j)    

while True:                                                 # store 리스트 중 공백 문자열 제거
    try:
        store.remove("")
    except ValueError:
        break        

print(store)
print('='*50)
print(len(store))