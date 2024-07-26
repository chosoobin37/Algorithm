total=int(input())
num=int(input())

sum = 0
for i in range(1, num+1):
    price, count = map(int, input().split())
    sum += price*count

if sum == total:
    print('Yes')
else:
    print('No')