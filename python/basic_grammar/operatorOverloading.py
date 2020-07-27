# 연산자 오버로딩 : 부모 클래스에서 정의한 메소드 말고 자식 클래스에서 정의한 메소드를 사용하고 싶을때
#               메소드를 새롭게 정의해서 사용할 수 있는데 이를 오버로딩이라고 한다.

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(
#             self.name, location, self.speed))

# # 공격 유닛


# class AttackUnit(Unit):  # Unit을 상속 받는다.
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)  # Unit의 내용을 가져온다.
#         self.damage = damage

#     # attack 메소드
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(
#             self.name, location, self.damage))

#     # damaged 메소드
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기. 마린/파이어뱃/탱크 등 지상 유닛들을 수송. 공격은 할 수 없음

# # 날 수 있는 기능을 가진 클래스


# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(
#             name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# # 만약 레이스 같은 경우는 공격도 할 수 있고 날 수도 있어야 한다.
# # 그래서 AttackUnit, Flyable을 상속 받는다.


# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
#         Flyable.__init__(self, flying_speed)


# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")

# 하지만 위의 코드에서 문제는 지상 유닛 경우 move()를 써야하고 공중 유닛 경우 fly() 함수를 사용해야 한다.
# 그래서 매번 지상 유닛인지 공중 유닛인지를 확인해야 한다.
# 이때 연산자 오버로딩을 통해서 똑같이 move() 함수만 사용하면 지상 유닛일 경우 이동을 하고 공중 유닛일 경우
# 에는 날아 갈 수 있도록 처리를 해야한다.

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(
            self.name, location, self.speed))


class AttackUnit(Unit):  # Unit을 상속 받는다.
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)  # Unit의 내용을 가져온다.
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(
            self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(
            name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):  # move() 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


vulture = AttackUnit("벌쳐", 80, 10, 20)

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")
