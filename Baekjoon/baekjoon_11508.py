import sys
input = sys.stdin.readline

num = int(input())
dairy = []


for i in range(num):
    drink = int(input())
    dairy.append(drink)

cost = 0

dairy.sort(reverse=True)

# while dairy:
for i in range(num // 3):
    if len(dairy) > 3:
        cost += dairy[i] + dairy[i+1]
        dairy.remove(dairy[i])
        dairy.remove(dairy[i+1])
        dairy.remove(dairy[i+2])
    elif len(dairy) == 2:
        cost += dairy[i] + dairy[i+1]
        dairy.remove(dairy[i])
        dairy.remove(dairy[i+1])
    elif len(dairy) == 1:
        cost += dairy[i]
        dairy.remove(dairy[i])

print(cost)