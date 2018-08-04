from flask import Flask, request, url_for, render_template, redirect, jsonify
from config import webConfig
from model.dbMgr import searchSql,MarketInfoSql,searchMarketNameSql,searchMarketScore
 
app = Flask(__name__)
app.secret_key = 'dlghkdhlrh'
config = webConfig()

@app.route('/')
def main():
        return render_template('main.html',name='맛있나역',config=config)

@app.route('/second', methods=['GET', 'POST'])
def second():
    if request.method == 'POST':
        subway = request.form['subway']
        if subway[-1] == '역':
            subway = subway[0:-1]
        row = searchSql(subway)
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

# @app.route('/third', methods=['GET','POST'])
# def detail():
#     if request.method == 'GET':
#         market = request.args.get('marketName')
#         marketName = MarketInfoSql(market)
#         return render_template('third.html',marketName=marketName)

@app.route('/third/<num>', methods=['GET','POST'])
def market_info(num):
    if request.method == 'GET':
        marketName = MarketInfoSql(num)
        return render_template('third.html',marketName=marketName)

if __name__ == '__main__':
    app.run(debug=config.debug)