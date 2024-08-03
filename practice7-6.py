gun = 10

def checkpint(soldiers):
    global gun  # 전역변수 gun을 참조
    gun = gun - soldiers
    print(f"[함수 내] 남은 총: {gun}")

def checkpointRet(gun, soldiers):
    gun = gun - soldiers
    print(f"[함수 내] 남은 총: {gun}")
    return gun

print(f"전체 총: {gun}")
# checkpint(2)
gun = checkpointRet(gun, 2)
print(f"남은 총: {gun}")