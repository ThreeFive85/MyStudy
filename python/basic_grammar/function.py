def open_account():
    print("Creat new account")


# 함수는 실제로 호출을 하기 전까지는 실행이 되지 않는다.
open_account()

# 전달값과 반환값


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance+money


balance = 0
balance = deposit(balance, 1000)
print(balance)


def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance


# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 1000)

def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    return commission, balance - money - commission


commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

# 함수 기본값

# def profile(name, age, main_lang):
#     print("이름 : {0}, 나이 : {1}, 주 사용 언어 : {2}".format(name, age, main_lang))


# profile("hulk", 20, "python")
# profile("ironman", 25, "c++")

def profile(name, age=17, main_lang="python"):
    print("이름 : {0}, 나이 : {1}, 주 사용 언어 : {2}".format(name, age, main_lang))


profile("hulk")
profile("spiderman")
profile("ironman", 21, "c++")

# 키워드 값


def profiles(name, age, main_lang):
    print(name, age, main_lang)


profiles(age=25, name="thor", main_lang="java")
profiles(main_lang="javascript", name="strange", age=30)

# 가변인자 (인자의 갯수가 정해져 있지 않을 때)


def profile1(name, age, *language):
    print("이름 : {0}, 나이 : {1}, ".format(name, age),
          end=" ")  # end=" "는 프린트 문을 줄바꿈하지 않고 이어서 출력
    for lang in language:
        print(lang, end=" ")
    print()


profile1("ironman", 20, "java", "python", "c++")
profile1("hulk", 25, "kotlin", "swift")

# 지역변수, 전역변수
# 지역변수는 지정한 함수 내에서만 사용
# 전역변수는 모든 범위에서 사용
gun = 10


def checkpoint(soldiers):  # 경계근무
    global gun  # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
# checkpoint(2)  # 2명이 경계 근무를 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
