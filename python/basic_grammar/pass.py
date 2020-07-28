# pass : 아무것도 하지 않고 일단은 넘어간다는 의미

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
        pass


# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
# BuildingUnit 클래스에 pass를 해놓고 클래스를 사용하여 supply_depot을 만들고 실행을 해보면
# 별 다른 에러 동작 없이 프로그램이 종료된다. 이렇게 pass는 어떠한 동작을 하지 않고 일단은 넘어 간다는 의미이다.

# 또 다른 예제로 두 개의 함수를 만들어 사용해 보자


def game_start():
    print("[알림] 새로운 게임을 시작합니다")


def game_over():
    pass


game_start()
game_over()
# 위 2개의 함수를 호출해보면 game_start() 함수는 실행이 되고 game_over() 함수는 pass를 했기 때문에
# 그냥 넘어가는 것을 볼 수 있다.
