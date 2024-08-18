# 사용자 정의 예외처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력 하세요: "))
    num2 = int(input("두 번째 숫자를 입력 하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError(f"입력값: {num1}, {num2}")
    print(f"{num1} / {num2} = {int(num1 / num2)}")
except ValueError:
    print("잘못된 값을 입력 하였습니다. 한 자리 숫자만 입력 하세요.")
except BigNumberError as err:
    print("에러가 발생 하였습니다. 한 자리 숫자만 입력 하세요.")
    print(err)