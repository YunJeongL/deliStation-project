'''
파이썬에서 maria db를 접속하고, 쿼리 수행
1. 접속, 해제
2. 쿼리수행 : 쿼리(Query)는 데이터베이스를 조작하는 언어
   conn.cursor()는 pymysql에서 쿼리 수행을 위해서 사용하는 객체임
3. 기본 커서는 데이터를 오직 순서대로만 보내기 때문에 
   테이블 컬럼의 위치가 변경되거나, 쿼리문이 조정되면
   순서가 바뀌게 되서 소스를 수정해야하는 상황이 벌어진다
   => 해결방안 : 컬럼이 따라와서 딕셔너리 형태로 가면 순서가 의미 없으므로 자동으로 해결된다
4. 쿼리문에 인자를 전달하여 수행하기 -> 일반화 기본작업
5. with문을 이용하여 커서 닫기를 자동으로 처리
6. 함수화를 통해서 누구나, 여러번 호출만으로 이 기능을 사용하게 처리
7. 함수에 리턴값을 부여하여 쿼리 결과를 돌려주게 처리
8. 모듈화를 위한 처리
'''
import pymysql as my


# # 로그인 처리
# def loginSql(search):
#     rows = None
#     try:
#         # 디비 오픈
#         conn = my.connect(host='127.0.0.1',
#                             port = '3307',#(포트가 다른 사람은 변경),
#                             user='root',
#                             password='1234',
#                             db='pythondb',
#                             charset='utf8',
#                             cursorclass=my.cursors.DictCursor)
#         print('연결성공')
#         #####################################################
#         # 쿼리 수행 절차
#         # 1. 커서 획득
#         with conn.cursor() as cursor:
#             # 2. sql 준비
#             sql = '''
#             select 
#                 *
#             from 
#                 subway_name
#             '''
#             # %s => '값'
#             # 3. 쿼리 수행
#             cursor.execute(sql, (search)) 
#             # 4. select => 결과 집합이 리턴됨 => 결과 패치
#             rows = cursor.fetchall()
#             # 멀티라는, 즉 이름만 출력되게 작성
#             #print(rows)
#             #for row in rows:
#             #    print(row['name'])
#             # 5. 커서 닫기 -> 자동처리
#             #cursor.close()
#         #####################################################
#         # 디비 닫기
#         conn.close()
#         print('닫기성공')

#     except Exception as e:
#         print(e)
    
#     #else
    
#     finally:
#         return rows

# 검색 처리
def searchSql(search):
    row = None
    try:
        # 디비 오픈
        conn = my.connect(host='127.0.0.1',
                            port =3306,#(포트가 다른 사람은 변경),
                            user='root',
                            password='1234',
                            db='pythondb',
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        # 쿼리
        with conn.cursor() as cursor:
            sql = "select name from subway_name where name like '%{0}%';".format(search)
            cursor.execute(sql) 
            roww = cursor.fetchone()
            row=roww['name']
        
        # 디비 닫기
        conn.close()

    except Exception as e:
        print(e)
        row = None
    #else
    
    finally:
        return row

# 역별 top 10 음식점 불러오기        
def searchMarketNameSql(subway):
    rows = None
    marketList=[]
    try:
        # 디비 오픈
        conn = my.connect(host='127.0.0.1',
                            port =3306,#(포트가 다른 사람은 변경),
                            user='root',
                            password='1234',
                            db='pythondb',
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        # 쿼리
        with conn.cursor() as cursor:
            sql = "select name from subway_market where subway_name like '%{0}%';".format(subway)
            cursor.execute(sql) 
            rows = cursor.fetchall()
            for row in rows:
                marketlist = row['name']
                marketList.append(marketlist)
                # print(row['name'])
            # print(marketList)
        # 디비 닫기
        conn.close()
    finally:
        return marketList
        # pass

# 음식점 사진, 평점, 호불호등 불러오기
def searchMarketScore(marketName):
    rows = None
    marketScoreList=[]
    try:
        # 디비 오픈
        conn = my.connect(host='127.0.0.1',
                            port =3306,#(포트가 다른 사람은 변경),
                            user='root',
                            password='1234',
                            db='pythondb',
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        # 쿼리
        with conn.cursor() as cursor:
            sql = "select name,rate,taste from subway_market where name like '{0}';".format(marketName)
            cursor.execute(sql) 
            rows = cursor.fetchall()
            for row in rows:
                # print(row)
                marketScoreList.append(row)
            # print(marketList)
        # 디비 닫기
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
        # 디비 오픈
        conn = my.connect(host='127.0.0.1',
                            port = 3306,#(포트가 다른 사람은 변경),
                            user='root',
                            password='1234',
                            db='pythondb',
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        #####################################################
        # 쿼리 수행 절차
        # 1. 커서 획득
        with conn.cursor() as cursor:
            # 2. sql 준비
            sql = "select * from market_info where name like '{0}';".format(marketName)
            # %s => '값'
            # 3. 쿼리 수행
            cursor.execute(sql) 
            # 4. select => 결과 집합이 리턴됨 => 결과 패치
            row= cursor.fetchone()
            # 멀티라는, 즉 이름만 출력되게 작성
            print(row)
            #for row in rows:
            #    print(row['name'])
            # 5. 커서 닫기 -> 자동처리
            #cursor.close()
        #####################################################
        # 디비 닫기
        conn.close()
    except Exception as e:
        print(e)
    #else
    finally:
        return row
MarketInfoSql('벤투라커피로스터스')
# 가게 이름 불러
def selectSubName(name):
    rows = None
    try:
        # 디비 오픈
        conn = my.connect(host='127.0.0.1',
                            #port = 3307(포트가 다른 사람은 변경),
                            user='root',
                            password='1234',
                            db='pythondb',
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        # 쿼리
        with conn.cursor() as cursor:
            sql = "select * from subway where name=%s;"
            cursor.execute(sql, (name,)) 
            # fetchone() 1개만 가져온다 => 리스트 형태 제외됨
            rows = cursor.fetchone()
        
        # 디비 닫기
        conn.close()

    except Exception as e:
        print(e)
        rows = None
    #else 
    
    finally:
        return rows
    
    

    
# # 모든 팀 가져오기
# # (정렬기준 컬럼, 정렬방식, 시작페이지, 한 페이지의 양)
# def selectAllSubList(stdCol='num', order='asc', page=0, amt=10):
#     rows = None
#     try:
#         # 디비 오픈
#         conn = my.connect(host='127.0.0.1',
#                             port = 3307,#(포트가 다른 사람은 변경),
#                             user='root',
#                             password='1234',
#                             db='pythondb',
#                             charset='utf8',
#                             cursorclass=my.cursors.DictCursor)
#         # 쿼리
#         with conn.cursor() as cursor:
#             sql = '''select num, name from subway 
#             order by %s %s 
#             limit %s, %s;''' %(stdCol, order, page, amt)
#             cursor.execute(sql) 
#             rows = cursor.fetchall()
        
#         # 디비 닫기
#         conn.close()

#     except Exception as e:
#         print(e)
#         rows = None
#     #else
    
#     finally:
#         return rows


# 테스트 코드는 if문 이하로 이동 : 모듈화 처리 중 불필요한 코드 이동
if __name__ == '__main__':
    # results = selectSubName('역삼역')
    # results = selectAllSubList()
    # print('결과 :', results)
    searchMarketNameSql('역삼')
