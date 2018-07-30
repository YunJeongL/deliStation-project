from selenium import webdriver 
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

k = []
store = []
file = open('mar.csv','r')     # 가게이름 csv파일 경로 
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




url = "https://www.instagram.com/explore/tags/샘밭막국수/"      # url검색을 통해 검색창으로 바로 이동

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

driver.implicitly_wait(1) 

driver.get(url)
# totalCount = driver.find_element_by_class_name('-nal3 ').find_element_by_class_name('g47SY  ').text   #게시물수

#print(store)

for i in store:
    #print(i)
    driver.find_element_by_xpath('/html/body//span[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(i);
    time.sleep(1.3)
    try:
        count = driver.find_element_by_xpath('/html/body//span[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[2]/span/span').text
        driver.find_element_by_xpath('/html/body//span[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').clear();    wait = WebDriverWait(driver, 10)
        insta=[i,count.replace(",","")]
        print(insta)

    except:
        count='None'

    with open('insta_k.csv', 'a') as f:
        f.write(str(insta)+'\n')
        f.close()
        print('Output')
    # driver.find_element_by_xpath("""//*[@class="js not-logged-in client-root"]/body/span/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a""").send_keys(Keys.ENTER)
    # driver.find_element_by_xpath('/html/body//span[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div//a[1]').click()
    # driver.find_element_by_xpath('/html/body//span[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').click()
    # totalCount = driver.find_element_by_class_name('-nal3 ').find_element_by_class_name('g47SY  ').text   #게시물수


    # insta[i]=totalCount

    #print(insta)
    #{'샘밭막국수': '4,028', '램하우스': '298', '서초장어타운': '142', '명동곰돌이': '246'} 이런 형식으로 출력됨
    # with open('insCount.csv', 'a', encoding='utf-8-sig') as f:  # Just use 'w' mode in 3.x #딕셔너리 ziip csv파일로 만들기
    #     f.wirte(str())