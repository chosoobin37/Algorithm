num = int(input())
money = []
total = 0

for i in range(num):
    coin = int(input().strip())
    if coin == 0:
        money.pop()
    else:
        money.append(coin)

total = sum(money)

print(total)