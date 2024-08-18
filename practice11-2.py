# 패키지: 모듈들을 모아둔 파일
# import travel.thailand
# # import travel.thailand.ThilandPackege
# trip_to = travel.thailand.ThilandPackege()
# trip_to.detail()

from travel.thailand import ThilandPackege
trip_to = ThilandPackege()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackege()
trip_to.detail()