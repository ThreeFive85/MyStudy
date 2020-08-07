# 모듈 : 유지보수를 쉽고 코드의 재사용을 쉽게 할 수 있다.
# 파이썬에서는 함수 정의나 클래스등의 파이썬 문장들을 담고 있는 파일을 모듈이라고 한다.
# 모듈은 확장자가 .py 이다.

# 현재 파일에서 사용할 함수들을 정의한다.

# 일반 가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))

# 조조 할인 가격


def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))

# 군인 할인 가격


def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))
