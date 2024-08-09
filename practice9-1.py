# 클래스

# 마린: 공격, 군인, 총을 쏠 수 있음
# name = "마린"
# hp = 40
# damage = 5

# print(f"{name} 유닛이 생성되었습니다.")
# print(f"체력 {hp}, 공격력 {damage}\n")

# # 탱크: 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반/시즈 모드
# tankName = "탱크"
# tankHp = 150
# tankDamage = 35

# print(f"{tankName} 유닛이 생성되었습니다.")
# print(f"체력 {tankHp}, 공격력 {tankDamage}\n")

# tankName2 = "탱크"
# tankHp2 = 150
# tankDamage2 = 35

# print(f"{tankName2} 유닛이 생성되었습니다.")
# print(f"체력 {tankHp2}, 공격력 {tankDamage2}\n")

# def attack(name, loccation, damage):
#     print(f"{name}: {loccation} 방향으로 적군을 공격 합니다. [공격력 {damage}]")

# attack(name, "1시", damage)
# attack(tankName, "1시", tankDamage)
# attack(tankName2, "1시", tankDamage2)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} 유닛이 생성 되었습니다.")
        print(f"체력 {hp}, 공격력 {damage}")

marime1 = Unit("마린", 40, 5)
marime2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)