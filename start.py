from flask import Flask, render_template, redirect, url_for, session, request ,jsonify
# 환경설정 클래스 모듈 가져오기
from config import webconfig
# from service.model.dbMgr import loginSql, searchSql, selectAllEplList

app = Flask(__name__)
# 세션생성에 필요한 세션키(중복되지 않는 해쉬값)를 정의
app.secret_key = 'kimchaeyeon'
config = webconfig()


# 세션이 없어도 접근 가능한 페이지는 오직 로그인 으로 둔다.
# 세션 생성, 세션 종료, 세션 체크

# # 로그인
# @app.route('/login',methods=['POST','GET'])# 레스트풀 방식
# def login():
#     if request.method =='GET':
#         return render_template('login.html', config=config)
#     else:
#         uid  = request.form['uid']
#         upw  = request.form['upw']
#         row = loginSql(uid, upw)
#         # false: [],(),{},0,"" 
#         # row => Dict => {}
#         if row: # 회원이면 / 딕셔너리 안에 들어있으면
#             # 세션처리 (필요한 정보를 세션으로 저장한다)
#             # 사용자 아이디와 이름 저장하겠다
#             session['uid'] = uid
#             session['name'] = row['name']
#             return redirect( url_for('home') )
#         else:
#             return render_template('common/alert.html', msg='회원 아님')

# 홈페이지
@app.route('/main')
def main():
    return render_template('main.html',name= '맛있나역')
    
# # 로그아웃
# @app.route('/logout')
# def logout():
#     if not 'uid' in session:
#         return redirect( url_for('login') )
#     # 세션 종료
#     print( session )
#     print('*'*50 )
#     if 'uid' in session:
#         session.pop('uid', None)
#     if 'name' in session:
#         session.pop('name', None)
#     print('세션 제거 후->', session)

#     # 페이지 요청을 리다이렉트 -> 홈페이지
#     return redirect( url_for('home') )
    
# eplList
@app.route('/eplList')
def eplList():
    # 세션체크
    #if not 'uid' in session: # 세션 없으면 false -> 부정 -> 참 ->
    #    return redirect( url_for('login') )
    # 데이터 획득
    amt = 5;# 한 번에 보여 줄 양
    tmp = request.args.get('page')
    page = 0
    if tmp: # 전달 된 페이지가 있다면 ex) eplList?page=2,
            # 페이지 계산 2로 전달되면 1로 계산해야함( 쿼리 기준 )
        page = int(tmp) -1 ;
    # 최종 결과 획득
    rows = selectAllEplList( page = page*amt )
    # 화면 처리
    return render_template('eplList.html', config = config, epls = rows)

@app.route('/search',methods=['POST'])
def search():    
    keyword = request.form['keywordkey']
    print(keyword)
    tmp     = searchSql( keyword )
    print( tmp)
    if tmp == None: tmp=[]
    return jsonify(tmp)

if __name__=='__main__':
    app.run(debug = config.debug)
