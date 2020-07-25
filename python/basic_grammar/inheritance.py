# 상속

# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 공격 유닛


class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    # attack 메소드
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(
            self.name, location, self.damage))

    # damaged 메소드
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 위의 코드에서 Unit 과 AttackUnit에서 중복된 부분이 있다. name, hp
# 이때 AttackUnit은 Unit의 name, hp를 상속 받아 사용할 수 있다.


class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print("{0} 유닛이 생성 되었습니다.".format(self.name))

# 공격 유닛


class AttackUnit(Unit):  # Unit을 상속 받는다.
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)  # Unit의 내용을 가져온다.
        self.damage = damage

    # attack 메소드
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(
            self.name, location, self.damage))

    # damaged 메소드
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
