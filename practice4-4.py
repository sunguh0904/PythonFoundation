# print("a" + "b")
# print("a", "b")

# 방법 1

""" 
문자열이 끝난 후 % 정수를 넣어주면 문자열 속에 들어간 %d에 값이 들어간다.
%d에서 d는 정수만 삽입이 가능하다.
 """
print("나는 %d살 입니다." % 20) # %d: 정수 값을 넣겠다는 뜻(decimal)
print("나는 %s을 좋아해요." % "파이썬") # %s: 문자열 값을 넣겠다는 뜻(String)
print("Apple 은 %c로 시작해요." % "A") # %c: 캐릭터 값(한 글자)을 받겠다는 뜻(character)

# %s
print("나는 %s살 입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 순서대로 대입한다.

# 방법 2
print("나는 {}살 입니다.".format(20)) # format의 값을 문자열 중괄호에 대입한다.
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # format의 index 값을 대입한다.

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간")) # format에 변수를 지정하여 대입가능
print("나는 {age}살이며, {color}색을 좋아해요".format(color = "빨간", age = 20))

# 방법 4 (v.3.6 이상 사용 가능)
age = 29;
color = "파란";
print(f"나는 {age}살이며, {color}색을 좋아해요") # 문자열 앞에 f를 선언하면 실제 변수를 가져다 사용 가능

