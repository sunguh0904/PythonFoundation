# while
# customer = "토르"
# index = 5
# while index >= 1:
#     print(f"{customer}, 커피가 준비 되었습니다. {index} 번 남았어요")
#     index -= 1
#     if index == 0:
#         print("커피를 폐기 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print(f"{customer}, 커피가 준비 되었습니다. {index} 번 남았어요")
#     index += 1

customer = "토르"
person = "Unknown"

while person != customer:
    print(f"{customer}, 커피가 준비 되었습니다.")
    person = input("이름이 어떻게 되세요?")
