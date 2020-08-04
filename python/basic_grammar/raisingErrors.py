# 의도적인 예러 발생시키기

# 이번에 만들 계산기는 한자리 숫자에 대해서만 나눗셈을 허용하는 프로그램이다.
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")

# 위 코드에서 10보다 큰 수가 입력되면 raise를 사용하여 의도적으로 에러처리를 사용할 수 있다.


# 사용자 정의 예외처리
# 위에서 사용한 ValueError등은 파이썬에서 제공되는 에러다.
# 하지만 자신이 직접 만들어 사용할 수도 있다.

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
except BigNumberError as err:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
    print(err)

# 위 코드에서는 문제가 발생했을 때 직접 정의한 BigNumberError에 메세지를 던져주고
# BigNumberError에서는 메세지를 가지고 있다가
# except구문에서 처리가 될때 메세지를 받아와 출력을 해준다.
# 이렇게 해서 사용자는 자신이 무슨 값을 입력하여 오류가 발생하였는지를 알 수 있다.
