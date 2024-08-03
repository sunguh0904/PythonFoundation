def openAccount():
    print("새로운 계좌가 생성 되었습니다.")

def deposit(balance, money):
    print(f"입금이 완료 되었습니다. 잔액은 {balance + money} 원 입니다.")
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print(f"출금이 완료 되엇습니다. 잔액은 {balance - money} 원 입니다.")
        return balance - money
    else:
        print(f"출금이 완료되지 않았습니다. 잔액은 {balance} 원 입니다.")
        return balance
    
def withdrawNight(balance, money):
    commission = 100
    return commission, balance - money - commission
    
balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
commission, balance = withdrawNight(balance, 500)
print(f"수수료 {commission} 원 이며, 잔액은 {balance} 원 입니다.")