# pickle
""" 
프로그램 상에서 우리가 사용하는 데이터를 파일 형태로 저장
누군가가 파일을 가져와서 pickle을 사용해서 코드에 사용
 """

import pickle
# profileFile = open("profile.pickle", "wb")  # b: 바이너릴 타입, pickle을 사용하기 위해선 항상 사용, 인코딩 설정을 해줄필요는 없음
# profile = {"이름" : "박명수", "나이" : "30", "취미" : ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profileFile)   # profile에 있는 정보를 file에 저장
# profileFile.close()

profileFile = open("profile.pickle", "rb")
profile = pickle.load(profileFile)  # pickle.load: 파일에 있는 정보를 가지고와서 데이터 형태로 불러오기
print(profile)
profileFile.close()