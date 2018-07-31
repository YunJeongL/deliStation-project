'''
파이썬에서 mariadb를 접속하고, 쿼리 수행
1. 접속, 해제
2. 쿼리수행:쿼리(Query)는 데이터베이스를 조작하는 언어
   conn.cursor()는 pymysql에서 쿼리 수행을 위해서 사용
   하는 객체임 
3. 기본 커서는 데이터를 오직 순서대로만 보내기 때문에
   테이블 컬럼의 위치가 변경되거나, 쿼리문이 조정되면
   순서가 바뀌게 되서 소스를 수정해야 하는 상황이 벌어진다
   => 해결방안 => 컬럼이 따라와서 딕셔너리 형태로 가면
   => 순서가 의미 없으므로 자동으로 해결된다
4. 쿼리문에 인자를 전달하여 수행하기 -> 일반화 기본 작업
5. with문을 이용하여 커서 닫기를 자동으로 처리
6. 함수화를 통해서 누구나, 여러번 호출만으로 이 기능을 
   사용하게 처리
7. 함수에 리턴값을 부여하여 쿼리 결과를 돌려주게 처리
8. 모듈화를 위한 처리
'''
import pymysql as my

#로그인 처리
def loginSql(uid, upw):
    rows = None
    try:
        # 디비 오픈
        conn = my.connect(host='127.0.0.1',
                            #port='3307', 포트가 다른 사람을 변경
                            user='root',
                            password='1234',
                            db='pythondb', 
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        #print('연결 성공')
        #############################################
        # 쿼리 수행 절차
        # 1. 커서 획득
        with conn.cursor() as cursor:
            # 2. sql 준비
            sql = '''
                select
                    * 
                from
                    tbl_users
                where
                    uid=%s and upw=%s;
            '''
            # %s => '값'
            # 3. 쿼리 수행
            cursor.execute( sql, (uid, upw) )
            # 4. select => 결과 집합이 리턴됨 => 결과 패치
            rows = cursor.fetchone()  #아이디는 고유값이니까 all 안하고 one 해도 됨
            # 멀티라는 즉 이름만 출력되게 작성
            #print( rows )
            #for row in rows:
            #    print( row['name'] )
            # 5. 커서 닫기 -> 자동처리
            #cursor.close()
        ############################################
        # 디비 닫기
        conn.close()
        #print('닫기 성공')
    except Exception as e:
        #print( e )
        rows = None
    #else:
    #finally:
    return rows

#검색 처리
def searchSql(keyword):
    rows = None #검색 결과를 받는 그릇, rows라는 변수를 사용하기 전에 초기화하는 것
    try:
        #디비 오픈
        conn = my.connect(host='127.0.0.1',
                            #port='3307', 포트가 다른 사람을 변경
                            user='root',
                            password='1234',
                            db='pythondb', 
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        #쿼리
        with conn.cursor() as cursor:  #쿼리와 결과를 돌려주는 것
            sql = "select rank, name from tbl_epl where name like '%{0}%';".format(keyword)
            cursor.execute( sql )
            rows = cursor.fetchall()  #rows에 결과가 담겼다

        # 디비 닫기
        conn.close()

    except Exception as e:       
        rows = None
    return rows

#팀 검색
def selectTeamName(teamName):
    rows = None #검색 결과를 받는 그릇
    try:
        #디비 오픈
        conn = my.connect(host='127.0.0.1',
                            #port='3307', 포트가 다른 사람을 변경
                            user='root',
                            password='1234',
                            db='pythondb', 
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        #쿼리
        with conn.cursor() as cursor:  #쿼리와 결과를 돌려주는 것
            sql = "select * from tbl_epl where name=%s;"
            cursor.execute( sql ,(teamName, ) ) #sql 옆에는 ()는 튜플임
            #fetchall()하면 딕셔너리의 리스트 형태로 나옴 
            # -> fetchone()하면 한개만 딕셔너리로 나옴
            rows = cursor.fetchone() 

        # 디비 닫기
        conn.close()

    except Exception as e:       
        rows = None
    return rows

#팀 정보 수정 (총 경기 수만)
def updateTeamInfo(total, teamName):
    result = None #검색 결과를 받는 그릇
    try:
        #디비 오픈
        conn = my.connect(host='127.0.0.1',
                            #port='3307', 포트가 다른 사람을 변경
                            user='root',
                            password='1234',
                            db='pythondb', 
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        #쿼리
        with conn.cursor() as cursor:  #쿼리와 결과를 돌려주는 것
            sql = "update tbl_epl set total=%s where name=%s"
            cursor.execute( sql ,(total, teamName) ) #sql 옆에는 ()는 튜플임
           
        #커밋(디비에 실제 반영)
        conn.commit()
        #영향받은 row의 수로 설정 = 수정된 row의 수
        result = conn.affected_rows()
        # 디비 닫기
        conn.close()

    except Exception as e:       
        result = None
    return result

#모든 팀 가져오기
#(정렬기준컬럼, 정렬방식, 시작페이지, 한페이지의 양)
def selectAllEplList(stdCol='rank', order='asc', page=0, amt=5):
    rows = None #검색 결과를 받는 그릇
    try:
        #디비 오픈
        conn = my.connect(host='127.0.0.1',
                            #port='3307', 포트가 다른 사람을 변경
                            user='root',
                            password='1234',
                            db='pythondb', 
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
        #쿼리
        with conn.cursor() as cursor:  #쿼리와 결과를 돌려주는 것
            sql = '''select rank, name, winPoint, win from tbl_epl 
order by %s %s
limit %s, %s ;''' % (stdCol, order, page, amt)
            cursor.execute( sql ) #sql 옆에는 ()는 튜플임
            #fetchall()하면 딕셔너리의 리스트 형태로 나옴 
            # -> fetchone()하면 한개만 딕셔너리로 나옴
            rows = cursor.fetchall() 

        # 디비 닫기
        conn.close()

    except Exception as e:       
        rows = None
    return rows
    

# 테스트 코드는 if문 이하로 이동:모듈화 처리중 불필요한 코드이동
if __name__ == '__main__':
    # 함수에 아이디 비번넣어서 회원여부 조회 결과를 받는다
    #results = loginSql('2','2')
    # results = selectTeamName('번리 FC')
    results = updateTeamInfo('1000', '번리 FC')
    results = selectAllEplList()
    print( '결과:', results )

