from flask import Flask, render_template, redirect, url_for, session, request, jsonify
#환경설정 클래스 모듈 가져오기
#from service.config import WebConfig
from service.model.dbMgr import loginSql, searchSql, selectAllEplList


app = Flask(__name__)
#세션생성에 필요한 세션 키(중복되지 않는 헤쉬 값을 사용)를 정의
app.secret_key = 'asdgashdfgsdfgsga'
#config = WebConfig()

#홈페이지
@app.route('/')
def third_page():
    return render_template('3page.html')



if __name__=='__main__':
    app.run(debug=True)