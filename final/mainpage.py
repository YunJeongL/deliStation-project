from flask import Flask, request, url_for, render_template, redirect, jsonify
from config import webConfig
from model.dbMgr import searchSql,MarketInfoSql,searchMarketNameSql,searchMarketScore
 
app = Flask(__name__)
app.secret_key = 'dlghkdhlrh'
config = webConfig()

# @app.route('/')
# def home():
#     return render_template(url_for('main'), name='맛있나역')
  
@app.route('/')
def main():
    # if request.method == 'GET':
        return render_template('main.html',config=config)
    # else:
    #     search = request.form['subway']
    #     row = searchSql(search)
    #     if '#box' == '%역%':
    #         return '''
    #     <script>
    #         alert("%s");     //팝업 띄우기
    #         history.back();  //이전 페이지 이동
    #     </script>
    #     ''' % '"역"을 뺀 이름으로 검색해주세요'
    #     # if false : [], (), {}, 0, ""
    #     # row => dict => {}
    #     if row : 
    #         # 세션처리(필요한 정보를 세션으로 저장한다)
    #         # 사용자 아이디와 이름 저장하겠다
    #         return  render_template('second.html',search=row['name'])
    #     else :
    #         return render_template('/common/alert2.html', msg='역이름으로 검색해주세요')

@app.route('/second', methods=['GET', 'POST'])
def second():
    if request.method == 'POST':
        subway = request.form['subway']
        if subway[-1] == '역':
            subway = subway[0:-1]
        row = searchSql(subway)
        # if '#box' == '%역%':
        # <script>
        #         return '''
        #     alert("%s");     //팝업 띄우기
        #     history.back();  //이전 페이지 이동
        # </script>
        # ''' % '"역"을 뺀 이름으로 검색해주세요'
        # # if false : [], (), {}, 0, ""
        # # row => dict => {}
        # # subway = subway # 어떻게 역을
        # # marketList = searchMarketNameSql(subway)
        # # marketScoreList = searchMarketScore(marketName)
        # # marketList=marketList, market=marketScoreList
        marketList = searchMarketNameSql(subway) #역별 top10 맛집 불러오는 sql 코드
        marketInfo=[]
        for market in marketList:
            marketScoreList = searchMarketScore(market)
            marketInfo.append(marketScoreList)
        if row :
            return render_template('second.html', subway=row, marketInfoList=marketInfo)
        else:
            return render_template('/common/alert2.html', msg='역이름으로 검색해주세요')
    else:
        pass

# @app.route('/second', methods=['GET', 'POST'])
# def join():
#     # 채연 이해중 row = searchMarketNameSql(search)
#     if request.method == 'GET':
#         if 'search':
#             return render_template('second.html', name='%s')
#             amt =10;  # 한번에 보여줄 양(한페이지에 5개 보여줌)
#             tmp = request.args.get('page')
#             page = 0  # 최종 페이지값 초기값
#             if tmp:  # 전달된 페이지가 있다면(인자값이 전달되면 참) ex) eplList?page=2,...
#                 # 페이지 계산 2로 전달되면 1로 계산해야함(쿼리기준)
#                 page = int(tmp) - 1 ;
#             # 최종 결과 획득    
#             rows = selectAllSubList(page=page*amt)
#             # 화면처리
#             return render_template('second.html', config=config, epls=rows)
#     else:
#         print(request.form)
#         # subway = request.form['subway']
#         rows = searchSql(subway)
#         print(rows)
#         if rows:
#             return render_template('second.html', search=subway)
#         else:
#             return '''
#             <script>
#                 alert("정확한 역 이름으로 검색해주세요!");
#                 history.back();
#             </script>'''

@app.route('/third', methods=['GET','POST'])
def detail():
    if request.method == 'GET':
        market = request.args.get('marketName')
        marketName = MarketInfoSql(market)
        return render_template('third.html',marketName=marketName)

if __name__ == '__main__':
    app.run(debug=config.debug)