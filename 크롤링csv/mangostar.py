from selenium import webdriver as wd
import time
from urllib.request import urlopen # url 을 컨트롤하는 라이브러리 웹사이트 url을 열어주는
from bs4 import BeautifulSoup
MAIN_URL = 'http://www.mangoplate.com/'
driver   = wd.Chrome('/Users/kimchaeyeon/py_project/py_test/chromedriver.exe')
driver.get( MAIN_URL )
driver.implicitly_wait(0.5)
driver.find_element_by_id("main-search").send_keys('카페413프로젝트')
driver.find_element_by_class_name('btn-search').click()
driver.find_element_by_class_name('only-desktop_not').click()
html = driver.page_source 
soup = BeautifulSoup(html, 'html.parser')

# 평점 구하기
def ratePoint():
    ratePoint = soup.find('strong',{'class':'rate-point'})
    print(ratePoint.span.string)
ratePoint()

# 호불호
def tasteAll():
    GB = soup.find('section',{'class':'module review-container'})
    GB2 = GB.find_all('button',{'class':'review_fliter_item_btn'})
    TasteGood = GB2[1].text
    TasteSoso = GB2[2].text
    TasteBad = GB2[3].text
    print(TasteGood)
    print(TasteSoso)
    print(TasteBad)
tasteAll()

# 식당 관련된 해시 태그
# def restaurantTag():
#     restaurantTag = soup.find_all('a',{'class':'Restaurant__TagLink'})
#     i=restaurantTag.find_all('href')
#     for n in i:
#         print(n)
# restaurantTag()