# 스타크래프트 프로젝트 전반전
class Unit:
    def __init__(self, name, hp, spped):
        self.name = name
        self.hp = hp
        self.speed = spped
        print(f"{name} 유닛이 생성 되었습니다.")

    def move(self, location):
         print("[지상 유닛 이동]")
         print(f"{self.name}: {location} 방향으로 이동합니다. [속도: {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name}: {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name}: 현재 체력은 {self.hp}")
        if self.hp <= 0:
            print(f"{self.name}: 파괴되었습니다.")

class AttackUnit(Unit):
        def __init__(self, name, hp, damage, speed):
            Unit.__init__(self, name, hp, speed)
            self.damage = damage

        def attack(self, loccation):
             print(f"{self.name}: {loccation} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

# 마린
class Marine(AttackUnit):
    def __ini__(self):
          AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩: 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name}: 스팀팩을 사용합니다. (HP 10 감소)")
        else:
             print(f"{self.name}: 체력이 부족하여 스팀팩을 사용하지 않습니다.")

# 탱크
class Tank(AttackUnit):
    # 시즈모드: 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    seize_developed = False # 시즈모드 개발여부
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.sezie_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.sezie_mode == False:
            print(f"{self.name}: 시즈모드로 전환 됩니다.")
            self.damage *= 2
            self.sezie_mode = True
        
        # 현재 시즈모드일 때 -> 시즈모드 해제
            print(f"{self.name}: 시즈모드를 해제 합니다.")
            self.damage /= 2
            self.sezie_mode = False
        
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

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해제
            print(f"{self.name}: 클로킹 모드 해제 합니다.")
            self.clocked = False
        else: # 클로킹 모드 해제 => 모드 설정
            print(f"{self.name}: 클로킹 모드 설정 합니다.")
            self.clocked = True