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

# 건물


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # 지금까지 클래스를 상속 받아 초기화를 할 때는
        # Unit.__init__() 을 사용해 왔다.
        # 하지만 또 다른 방법으로는 super() 가 있다.
        super().__init__(name, hp, 0)  # super()로 초기화를 할 때는 self는 뺀다.
        self.location = location
# 이렇게 만듬으로써 Unit 클래스를 상속받는 BuildingUnit 클래스를 만들어 보았다.
# 하지만 super()는 다중 상속에서 문제점을 나타낸다.
# 2개 이상의 부모 클래스를 다중 상속 받을 때는 super()를 사용하면
# 순서 상의 맨 마지막에 상속 받는 클래스에 대해서만 __init__ 함수가 호출이 된다.
# 그래서 모든 부모 클래스에서 초기화가 필요할 때에는 super()를 사용하면 않된다.
