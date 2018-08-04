# pip install selenium
from selenium import webdriver as wd
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import itemgetter
import sys
import glob
import os


# 기본 접속 사이트
MAIN_URL='http://www.mangoplate.com/'
# 브라우저 띄우기
driver = wd.Chrome('/Users/kimchaeyeon/py_project/py_test/chromedriver.exe')
# 접속
driver.get(MAIN_URL)
# 그냥 2초 대기후 진행
driver.implicitly_wait(0.5)
subName= input('역이름 입력:')
driver.find_element_by_id('main-search').send_keys(subName)
# 검색 클릭
driver.find_element_by_class_name('btn-search').click()
# 가게명 가져오기
page=driver.current_url
html=urlopen(page)
soup=BeautifulSoup(html,"html.parser")
market_lists= soup.find_all('h2',{'class':'title'})
# print(market_lists)

market_names = [ i.text for i in market_lists ]
print(market_names)

# 파일로 저장하기
max_index=len(market_names)
output_file=sys.argv[1]
filewriter=open(output_file,'a') #append
filewriter.write(str(subName)+',')
for i in range(max_index):
    if i<(max_index):
        filewriter.write(str(market_names[i])+',')
    else:
        filewriter.write(str(market_names[i])+'\n')
filewriter.close()
print('Output')