from selenium import webdriver 
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
 
k = []
store = []
file = open('mar12_2.csv','r', encoding='utf-8-sig')     # 가게이름 csv파일 경로 
csvReader = csv.reader(file)                           #-sig: utf로 인코딩했을때 처음 나오는 형식 문자 제거 
for row in csvReader:
    k.append(row)    
file.close()                    

for i in k:                                                 # 이중 문자열 1개의 문자열로 만들기
    for j in i:
        # print(j)
        j = ''.join(j.split())                              #리스트의 단어 안의 공백 제거
        store.append(j)    

while True:                                                 # store 리스트 중 공백 문자열 제거
    try:
        store.remove("")
    except ValueError:
        break        

insta={}
for i in store:
    url = "https://www.instagram.com/explore/tags/{}/".format(i)

    driver = webdriver.Chrome(executable_path='./chromedriver.exe')

    driver.implicitly_wait(5) 

    driver.get(url)
    totalCount = driver.find_element_by_class_name('-nal3 ').find_element_by_class_name('g47SY  ').text 
    insta[i]=totalCount   #insta에 딕셔너리 형식으로 가공
#print(insta)
#{'샘밭막국수': '4,028', '램하우스': '298', '서초장어타운': '142', '명동곰돌이': '246'} 이런 형식으로 출력됨


with open('insCount.csv', 'w', encoding='utf-8-sig') as f:  # Just use 'w' mode in 3.x #딕셔너리 ziip csv파일로 만들기
    w = csv.DictWriter(f, insta.keys())
    w.writeheader()
    w.writerow(insta)





