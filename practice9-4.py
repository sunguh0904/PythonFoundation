# 메소드
class AttackUnit:
        def __init__(self, name, hp, damage):
            self.name = name
            self.hp = hp
            self.damage = damage

        def attack(self, loccation):
             print(f"{self.name}: {loccation} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

        def damaged(self, damage):
             print(f"{self.name}: {damage} 데미지를 입었습니다.")
             self.hp -= damage
             print(f"{self.name}: 현재 체력은 {self.hp}")
             if self.hp <= 0:
                  print(f"{self.name}: 파괴되었습니다.")

# 파이어뱃: 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 15)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)