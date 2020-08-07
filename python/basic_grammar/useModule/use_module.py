# 앞서 modole.py에서 만들 모듈을 불러 온다.
# import module
# module.price(3)  # 3명이서 영화를 보러 갔을 때 가격
# module.price_morning(4)  # 4명이서 조조 할인 영화 보러 갔을 때
# module.price_soldier(5)  # 5명의 군인이 영화를 보러 갔을 때

# import module as mv  # as를 사용하면 정의한 module을 mv로 호칭하여 사용할 수 있다.
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from module import *  # 정의한 module의 내용을 모두 사용하겠다는 의미
# price(3)
# price_morning(4)
# price_soldier(5)

# from module import price, price_morning  # 명시적으로 필요한 부분만을 설정 할 수도 있다.
# price(3)
# price_morning(4)

# 정의한 module에서 price_soldier만 사용하는데 price라는 호칭으로 사용하겠다는 의미
from module import price_soldier as price
price(5)
