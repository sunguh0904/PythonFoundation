# 모듈
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격

# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때

# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

# import theater_module as mv # as 뒤에 별칭을 붙여서 mv로 호출 가능
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# price_soldier(5)

from theater_module import price_soldier as ps
ps(5)