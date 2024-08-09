# 메소드 오버라이딩
class Unit:
    def __init__(self, name, hp, spped):
        self.name = name
        self.hp = hp
        self.speed = spped

    def move(self, location):
         print("[지상 유닛 이동]")
         print(f"{self.name}: {location} 방향으로 이동합니다. [속도: {self.speed}]")

class AttackUnit(Unit):
        def __init__(self, name, hp, damage, speed):
            Unit.__init__(self, name, hp, speed)
            self.damage = damage

        def attack(self, loccation):
             print(f"{self.name}: {loccation} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

        def damaged(self, damage):
             print(f"{self.name}: {damage} 데미지를 입었습니다.")
             self.hp -= damage
             print(f"{self.name}: 현재 체력은 {self.hp}")
             if self.hp <= 0:
                  print(f"{self.name}: 파괴되었습니다.")

# 드랍쉽: 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송(공격 불가)
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flyingSpped):
        self.flyingSpeed = flyingSpped

    def fly(self, name, loccation):
         print(f"{name}: {loccation} 방향으로 날아갑니다. [속도: {self.flyingSpeed}]")

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flyingSpeed):
        AttackUnit.__init__(self, name, hp, 0, damage)    # 지상 스피드 0
        Flyable.__init__(self, flyingSpeed)

    def move(self, location):
        print("[공중 유닛 증가]")
        self.fly(self.name, location)

# 벌쳐: 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저: 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")