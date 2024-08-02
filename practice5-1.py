# 리스트 []

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")   # append: 리스트 마지막에 추가
print(subway)

# 정형돈씨를 유재석과 조세호 사이에 태워봄
subway.insert(1, "정형돈")  # insert: 첫 번째 인수의 인덱스 순서에 두 번째 인수 값을 삽입
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # pop: 리스트 마지막 값을 삭제
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
numList = [5, 2, 4, 3, 1]
numList.sort()
print(numList)

# 역정렬도 가능
numList.reverse()
print(numList)

# 모두 지우기
# numList.clear()
print(numList)

# 다양한 자료형 함께 사용 가능
mixList = ["조세호", 20, True]
print(mixList)

# 리스트 확장
numList.extend(mixList)
print(numList)