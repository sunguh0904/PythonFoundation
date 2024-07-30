python = "Python is Amazing"
print(python.lower()) # 모든 문자를 소문자로 출력
print(python.upper()) # 모든 문자를 대문자로 출력
print(python[0].isupper()) # 해당 순서의 문자가 대문자인지 boolean 출력
print(python[1].isupper()) # 해당 순서의 문자가 소문자인지 boolean 출력
print(len(python)) # 문자열의 길이 반환 (공백 포함)
print(python.replace("Python", "Java")) # 첫 번째 인수를 찾아 두 번째 인수로 변환

index = python.index("n") # 해당 문자가 몇 번째인지 확인
print(index)

index = python.index("n", index + 1) # 앞에서 구한 index 반환 값에 + 1을 기준으로 n을 찾는다.
print(index)

print(python.find("n")) # 해당 변수의 n의 위치를 찾는다.

# find와 index의 차이
print(python.find("Java")) # 해당 변수에 찾는 값이 없을 경우 -1을 반환(이후 뒤 코드 실행 함)
# print(python.index("Java")) # 해당 변수에 Java라는 문자가 없기 때문에 에러 반환 후 프로그램 종료(이후 뒤 코드 실행 안 됨)
print("hi")

print(python.count("n")) # 해당 변수에 전달받은 인수 값이 몇번 등장하는지 카운트
