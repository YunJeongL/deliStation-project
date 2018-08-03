import pymysql as my

# 검색 처리
def searchSql(search):
    row = None
    try:
        conn = my.connect(host='127.0.0.1',
                            port =3307,
                            user='root',
                            password='1234',
                            db='pythondb',
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        with conn.cursor() as cursor:
            sql = "select name from subway_name where name like '%{0}%';".format(search)
            cursor.execute(sql) 
            roww = cursor.fetchone()
            row=roww['name']
        conn.close()

    except Exception as e:
        print(e)
        row = None
    finally:
        return row

# 역별 top 10 음식점 불러오기        
def searchMarketNameSql(subway):
    rows = None
    marketList=[]
    try:
        conn = my.connect(host='127.0.0.1',
                            port =3307,
                            user='root',
                            password='1234',
                            db='pythondb',
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        with conn.cursor() as cursor:
            sql = "select name from market_info where subway_name like '%{0}%';".format(subway)
            cursor.execute(sql) 
            rows = cursor.fetchall()
            for row in rows:
                marketlist = row['name']
                marketList.append(marketlist)
                # print(row['name'])
            # print(marketList)
        conn.close()
    finally:
        return marketList
        # pass

# 2페이지 음식점별 정보 불러오기
def searchMarketScore(marketName):
    rows = None
    marketScoreList=[]
    try:
        conn = my.connect(host='127.0.0.1',
                            port =3307,
                            user='root',
                            password='1234',
                            db='pythondb',
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        with conn.cursor() as cursor:
            sql = "select subway_name,num,name,img,address,rate,insta,taste,rank from market_info where name like '{0}';".format(marketName)
            cursor.execute(sql) 
            rows = cursor.fetchall()
            for row in rows:
                marketScoreList.append(row)
        conn.close()

    except Exception as e:
        print(e)
        rows = None
    finally:
        return marketScoreList

# 3페이지
def MarketInfoSql(marketName):
    row = None
    try:
        conn = my.connect(host='127.0.0.1',
                            port = 3307,
                            user='root',
                            password='1234',
                            db='pythondb',
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        with conn.cursor() as cursor:
            sql = "select num,name,address,phone,kind,price,parking,time,img,tag1,tag2,tag3,tag4,tag5,tag6,rank from market_info where num like '{0}';".format(marketName)
            cursor.execute(sql) 
            row= cursor.fetchone()
            print(row)
        conn.close()
    except Exception as e:
        print(e)
    finally:
        return row
# MarketInfoSql('벤투라커피로스터스')
    
# 테스트 코드는 if문 이하로 이동 : 모듈화 처리 중 불필요한 코드 이동
if __name__ == '__main__':
    # results = selectSubName('역삼역')
    # results = selectAllSubList()
    # print('결과 :', results)
    searchMarketNameSql('역삼')
