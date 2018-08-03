from flask import Flask, render_template, redirect, url_for, session, request ,jsonify
# 환경설정 클래스 모듈 가져오기
from config import webconfig
from dbMgr import searchSubway
# from service.model.dbMgr import loginSql, searchSql, selectAllEplList

app = Flask(__name__)
config = webconfig()


# 홈페이지
@app.route('/')
def home():
    return render_template('main.html', name='맛잇나역')
# 만약 여기에 아이디가 있다면 다음페이지로 넘어가기ㅑ
@app.route('/main')
def main():
    search  = request.form['search']
    row = searchSubway(search) #db에서 가져오기
    return render_template('page2.html',name= '맛있나역')
@app.route('/page2')
def page2():
    return render_template('main.html',name= '맛있나역')
@app.route('/page3')
def page3():
    return render_template('main.html',name= '맛있나역')
    
if __name__=='__main__':
    app.run(debug = config.debug)
