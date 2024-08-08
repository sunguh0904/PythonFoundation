# with

""" 
파일을 열고 닫기가 조금 더 편해짐
 """

import pickle
with open("profile.pickle", "rb") as profileFile:
    print(pickle.load(profileFile))

# close 필요없음

# with open("study.txt", "w", encoding="utf8") as studyFile:
#     studyFile.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as studyFile:
    print(studyFile.read())
