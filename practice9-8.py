# pass
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

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass
    
# 서플라이 디폿: 건물, 1개 건물 = 8 유닛 생성 가능
supplyDepot = BuildingUnit("서플라이 디폿", 500, "7시")

def gameStart():
     print("[알림] 새로운 게임을 시작합니다.")

def gameOver():
     pass   # 실행 오류를 방지할 때 사용, 그냥 넘어감

gameStart()
gameOver()