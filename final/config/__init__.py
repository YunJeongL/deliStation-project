class webConfig:
    # 멤버 변수
    title = '맛있나역'
    site_name = '역 주변 핫플레이스 정보 제공 사이트'
    version = 'v1.0.0'
    debug = True
    page_title = { 'LOGIN':'관리자 로그인', 'MENU1':'2017~18 eplList' }
    
    host = '127.0.0.1'
    port = 3307 # 포트가 다른 사람은 변경
    user = 'root'
    password = '1234'
    db = 'pythondb'
    charset = 'utf8'

    # 생성자
    def __init__( self ):
        print(' 환경설정 생성자 호출 ')
    # 멤버 함수
    
if __name__ == '__main__':
    obj = webConfig() 
    print( obj.site_name )