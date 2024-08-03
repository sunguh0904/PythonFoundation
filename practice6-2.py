# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4")

# for waitingNo in [0, 1, 2, 3, 4]:
for waitingNo in range(1, 6):
    print(f"대기번호: {waitingNo}")

starbucks = ["아이언맨", "토르", "스파이더맨"]
for customer in starbucks:
    print(f"{customer}, 커피가 준비되었습니다.")