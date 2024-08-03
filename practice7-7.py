""" 
Quiz:
표준 체중을 구하는 프로그램을 작성하시오
* 표준 체중: 각 개인의 키에 적당한 체중

(성별에 다른 공식)
남자: 키(m) x 키(m) x 22 (int)
여자: 키(m) x 키(m) x 21 (int)

조건1: 표준 체중은 별도의 함수 내에서 계산
        * 함수 명: std_weight
        * 전달 값: 키(height), 성별(gender)
조건2: 표준 체중은 소수점 둘 째 자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
 """

def std_weight(height, gender):
    if gender == "남자":
        return (height / 100) * (height / 100) * 22, height, gender
    else:
        return (height / 100) * (height / 100) * 21, height, gender
    
weight, height, gender = std_weight(155, "여자")

# weight = str(weight)[:str(weight).index(".") + 3]
weight = round(weight, 2)

print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.")