# 다중 상속
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
        def __init__(self, name, hp, damage):
            Unit.__init__(self, name, hp)
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
          AttackUnit.__init__(self, name, hp, damage)
          Flyable.__init__(self, flyingSpeed)

# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")