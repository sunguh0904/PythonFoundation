# 패키지, 모듈 위치

from travel import *
trip_to = thailand.ThailandPackege()
trip_to.detail()
import inspect  # inspect: 패키지나 모듈의 위치를 확인할 때 사용
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))