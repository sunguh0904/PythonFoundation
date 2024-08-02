cabinet = {
    3 : "유재석",
    100 : "김태호"
}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])     # 값이 없을 경우 에러 발생 후 이후 로직 종료
# print("hi")
# print(cabinet.get(5, "사용 가능"))    # 값이 없을 경우 none 또는 두 번째 인수의 문자를 반환 후 다음 로직 실행

print(3 in cabinet)     # 참일 경우 Ture, 아닐 경우 False

cabinet = {
    "A-3" : "유재석",
    "A-100" : "김태호"
}
print(cabinet.get("A-3"))
print(cabinet.get("A-100"))

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

#  간 손님
del cabinet["A-3"]
print(cabinet)

# key 만 출력
print(cabinet.keys())

# value 만 출력
print(cabinet.values())

# key, value 모두 출력
print(cabinet.items())

# 객체 초기화
print(cabinet.clear())