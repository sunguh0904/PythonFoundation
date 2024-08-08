# 파일 입출력
# score 라는 파일을 만들고, 쓰기만 가능하며, 인코딩 설정
# scoreFile = open("score.txt", "w", encoding="utf-8")
# print("수학: 0", file=scoreFile)
# print("영어: 50", file=scoreFile)
# scoreFile.close()   # 마지막은 파일 닫기

# scoreFile = open("score.txt", "a", encoding="utf-8")    # a: 이미 존재하는 파일에다가 덮어쓰기를 하고싶다면...(append) 사용
# scoreFile.write("과학: 80")
# scoreFile.write("\n코딩: 100")
# scoreFile.close()

# 파일에 있는 내용을 읽어오기
scoreFile = open("score.txt", "r", encoding="utf-8")    # r: 읽어오기
# print(scoreFile.read())
# print(scoreFile.readline(), end="")    # readline(): 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(scoreFile.readline(), end="")
# print(scoreFile.readline(), end="")
# print(scoreFile.readline(), end="")

# 해당 파일이 몇줄인지 모를 땐 반복문 사용하기
# while True:
#     line = scoreFile.readline()
#     if not line:
#         break
#     print(line, end="")

lines = scoreFile.readlines()   # list 형태로 저장
for line in lines:
    print(line, end="")

scoreFile.close()
