# print("Python", "Java")
# print("Python" + "Java")
print("Python", "Java", "JavaScript", sep=",", end="?")
# sep: 문자 사이의 콤마에 해당 값으로 바꿔달라
# end: 문장의 끝 부분을 물음표로 바꿔달라
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout)    # stdout: 표준 출력으로 문장이 찍히는 것
print("Python", "Java", file=sys.stderr)    # stderr: 표준 에러로 처리

# 출력 포멧
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # ljust(8): subject 라는 변수에 8칸의 공간을 만들어서 왼쪽 정렬
    # rjust(4): score 라는 변수에 4칸의 공간을 만들어서 오른쪽 정렬

# 은행 대기 순번표
# 001, 002, 003 ...
for number in range(1, 21):
    print("대기번호: " + str(number).zfill(3))
    # zfill(3): number 라는 변수에 3 크기 만큼의 공간을 확보 후 값을 넣는데, 값이 없는 공간에 대해서는 0 으로 처리

answer = input("아무 값이나 입력하세요: ")  # input: 사용자 입력 값으로 전달 받은 값은 모두 문자열로 처리됨
# print(type(answer))
print(f"입력하신 값은 " + answer + " 입니다.")