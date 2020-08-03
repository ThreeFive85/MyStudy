# 예외처리

# print("나누기 전용 계산기입니다.")
# num1 = int(input("첫 번째 숫자를 입력하세요 : "))
# num2 = int(input("두 번째 숫자를 입력하세요 : "))
# print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

# 만약 위의 코드에서 int가 아닌 str을 입력하게 된다면
# ValueError: invalid literal for int() with base 10: 'tka'
# 라는 에러를 내고 프로그램은 종료가 된다. 이렇게 숫자가 아닌 다른 값을 입력했을 때
# 오류를 처리하는 방법은 try를 사용하면 된다.

try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
# 만약 0을 나누기로 한다면?
except ZeroDivisionError as err:
    print(err)

# 만약 어떤 에러인지 표시 하고 싶을 때는
# except Exception as err:
#     print(err)
