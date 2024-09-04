import sys
input = sys.stdin.readline

num = int(input())
dairy = []

for i in range(num):
    drink = int(input())
    dairy.append(drink)

dairy.sort(reverse=True)

cost = 0

for i in range(len(dairy)):
    # 3번째 상품은 무료로 계산
    if i % 3 != 2:
        cost += dairy[i]

print(cost)