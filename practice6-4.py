absent = [2, 5] # 결석
boot = [7] # 책을 안 가져옴
for student in range(1, 11):
    if student in absent:
        continue
    elif student in boot:
        print(f"오늘 수업 여기까지, {boot}는 교무실로 따라와")
        break
    print(f"{student}, 책을 읽어봐")