from flask import Flask, request, url_for, render_template, redirect, jsonify
from config import WebConfig
from model.dbMgr import loginSql, searchSql, selectAllSubList
 
app = Flask(__name__)
app.secret_key = 'dlghkdhlrh'
config = WebConfig()

@app.route('/')
def home():
    return render_template('main.html', name='맛있나역')
    if '#box' == '%역%':
        return '''
        <script>
            alert("%s");     //팝업 띄우기
            history.back();  //이전 페이지 이동
        </script>
        ''' % '역 이름으로 검색해주세요'
@app.route('/', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('main.html',config=config)
    else:
        search = request.form['search']
        row = searchSql(search)
        # if false : [], (), {}, 0, ""
        # row => dict => {}
        if row : 
            # 세션처리(필요한 정보를 세션으로 저장한다)
            # 사용자 아이디와 이름 저장하겠다
            
            return redirect(url_for('/second'))
        else:
            return render_template('/alert2.html', msg='역이름으로 검색해주세요')

@app.route('/second', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        if 'search':
            return render_template('sb2.html', name='%s')
            amt =10;  # 한번에 보여줄 양(한페이지에 5개 보여줌)
            tmp = request.args.get('page')
            page = 0  # 최종 페이지값 초기값
            if tmp:  # 전달된 페이지가 있다면(인자값이 전달되면 참) ex) eplList?page=2,...
                # 페이지 계산 2로 전달되면 1로 계산해야함(쿼리기준)
                page = int(tmp) - 1 ;
            # 최종 결과 획득    
            rows = selectAllSubList(page=page*amt)
            # 화면처리
            return render_template('sb2.html', config=config, epls=rows)
    else:
        print(request.form)
        subway = request.form['subway']
        rows = searchSql(subway)
        print(rows)
        if rows:
            return render_template('sb2.html')
        else:
            return '''
            <script>
                alert("검색 결과가 없어서 되돌아갑니다!");
                history.back();
            </script>'''

if __name__ == '__main__':
    app.run(debug=config.debug)