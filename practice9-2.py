class Unit:
    def __init__(self, name, hp, damage):   # __init__: 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} 유닛이 생성 되었습니다.")
        print(f"체력 {hp}, 공격력 {damage}")

marime1 = Unit("마린", 40, 5)
marime2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)