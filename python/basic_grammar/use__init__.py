# __init__ 는 파이썬에서 쓰이는 생성자이다.

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


marin1 = Unit("마린", 40, 5)
marin2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 위의 코드에서 __init__은 마린, 탱크의 객체가 만들어질 때 자동으로 호출되는 부분이다.
# 마린, 탱크처럼 class로 부터 만들어진 것들을 객체라고 부른다. 이때 마린, 탱크는 Unit 클래스의 인스턴스이다.
# 객체를 표현할 때는 Unit에서 self를 제외한 name, hp, damage의 값을 주어야한다.
