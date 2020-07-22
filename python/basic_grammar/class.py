# 스타크래프트 게임을 예제로 class 사용법 공부

# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# marin_name = "마린"  # 유닛의 이름
# marin_hp = 40  # 유닛의 체력
# marin_damage = 5  # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다".format(marin_name))
# print("체력 {0}, 공격력 {1}".format(marin_hp, marin_damage))

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음, 일반 모드/ 시즈 모드
# tank_name = "탱크"  # 유닛의 이름
# tank_hp = 150  # 유닛의 체력
# tank_damage = 35  # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다".format(tank_name))
# print("체력 {0}, 공격력 {1}".format(tank_hp, tank_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))


# attack(marin_name, "1시", marin_damage)
# attack(tank_name, "1시", tank_damage)

# 만약 여기서 탱크나 마린이 하나 더 추가 된다면 또 다른 유닛을 설정해야한다. 유닛은 수백, 수천이 될수 있기때문에
# 일일이 유닛을 작성하는 것은 불가능하다. 그래서 이를 보안하기 위해 클래스를 사용한다.
# 클래스는 하나의 틀 형태로 서로 연관이 있는 변수와 함수의 집합 정도로 이해하면 된다.

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

# 하나의 클래스를 통해 서로 다른 유닛들을 생성할 수 있다.
