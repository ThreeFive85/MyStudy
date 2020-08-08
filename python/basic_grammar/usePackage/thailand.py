class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


# 모듈 직접 실행
# 현재까지 만들어 놓은 코드들은 매우 짧은 코드들이기 때문에 별다른 테스트 없이 바로 코드를 작성하였지만
# 하지만 실제로 패키지나 모듈을 만들때에는 모듈이 잘 동작하는지를 테스트를 해보아야한다.
# 그러기 위해서는 다음과 같은 방법을 사용할 수 있다.
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
    # 현재 모듈에서 직접 실행 할 경우 위의 구문과 함께 trip_to.detail()의 내용이 출력된다.
else:
    print("Thailand 외부에서 모듈 호출")
    # 만약 외부에서 모듈을 사용할 때에는 위 구문이 호출된다.
