""" 
Quiz: 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

예) http://naver.com
규칙1: http:// 부분은 제외 => naver.com
규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
                (nav)             (5)              (1)        (!)
예 생성된 비밀번호: nav51!
 """

url = "http://naver.com"
urlArr = url[url.index("/") + 2 : url.index(".")]
newUrlArr = urlArr[:3]
urlLen = len(urlArr)
urlCount = urlArr.count("e")
print(f"{url}의 비밀번호는 {newUrlArr}{urlLen}{urlCount}! 입니다.")