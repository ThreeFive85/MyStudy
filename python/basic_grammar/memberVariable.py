# 멤버 변수

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

# 멤버 변수는 class 내에서 정의된 변수이고, 그 변수를 가지고 초기화를 할 수 있고, 실제로 사용할 수도 있다.
# 위 class에서는 name, hp, damage가 멤버 변수이다.
# 멤버 변수의 접근은 .으로 접근할 수 있다.
print("유닛의 이름 : {0}, 공격력 : {1}".format(marin1.name, marin1.damage))

# 멤버 변수를 추가로 할당할 수도 있다.
wraith = Unit("레이스", 80, 5)
wraith.clocking = True

if wraith.clocking == True:
    print("{0}는 현재 클로킹 상태입니다".format(wraith.name))

# 만약 wraith2를 만들고 clocking을 추가로 할당하지 않았다면 wraith2에서는 clocking은 사용할 수 없다.
