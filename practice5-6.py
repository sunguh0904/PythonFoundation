""" 
Quiz:
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오

조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1 ~ 20 이라고 가정
조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3: random 모듈의 shuffle 과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자: 1
커피 당첨자: [2, 3, 4]
-- 축하합니다 --
 """

# (활용 예제)
from random import *
# list = [1, 2, 3, 4, 5]
# print(list)
# shuffle(list)   # shuffle: 리스트 안의 값의 순서를 무작위로 변경
# print(list)
# print(sample(list, 1))  #sample: 첫 번째 인수에서 두 번째 인수의 수 만큼 무작위로 출력

# idArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
idArr = range(1, 21)    # 1 부터 21 직전까지의 수를 생성
print(idArr, type(idArr))
idArr = list(idArr)
print(idArr, type(idArr))
shuffle(idArr)
print(idArr)

chicken = sample(idArr, 1)
print(chicken, type(chicken))
chicken = set(chicken)
print(chicken, type(chicken))

idArr = set(idArr)
print(idArr, type(idArr))
idArr = idArr.difference(chicken)
print(idArr)

coffe = sample(list(idArr), 3)
print(coffe)

chicken = list(chicken)
print(chicken, type(chicken))


print(f'''
    -- 당첨자 발표 --
    치킨 당첨자: {chicken[0]}
    커피 당첨자: {coffe}
    -- 축하합니다 --
''')