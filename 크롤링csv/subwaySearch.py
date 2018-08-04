# pip install selenium
from selenium import webdriver as wd
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import itemgetter
import sys
import glob
import os

# 망고플레이트 들어가기
MAIN_URL='http://www.mangoplate.com/'
driver = wd.Chrome('/Users/kimchaeyeon/py_project/py_test/chromedriver.exe')
driver.get(MAIN_URL)
driver.implicitly_wait(0.5)

# 역 불러오기
subName= input('역이름 입력')
driver.find_element_by_id('main-search').send_keys(subName)
driver.find_element_by_class_name('btn-search').click()
page=driver.current_url
html=urlopen(page)
soup=BeautifulSoup(html,"html.parser")
market_lists= soup.find_all('h2',{'class':'title'})

market_names = [ i.text for i in market_lists ]
print(market_names)

max_index=len(market_names)
output_file=sys.argv[1]
filewriter=open(output_file,'a') #append
for i in range(max_index):
    if i<(max_index-1):
        filewriter.write(str(market_names[i])+',')
    else:
        filewriter.write(str(market_names[i])+'\n')
filewriter.close()
print('Output')

