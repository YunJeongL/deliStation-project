from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html', name='맛있나역')
    if subway != '%역%':
        return '''
        <script>
            alert("%s");     //팝업 띄우기
            history.back();  //이전 페이지 이동
        </script>
        ''' % '역 이름으로 검색해주세요'

if __name__ == '__main__':
    app.run(debug=True)