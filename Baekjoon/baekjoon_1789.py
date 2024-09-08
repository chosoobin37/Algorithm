import sys
input = sys.stdin.readline

num = int(input())
sum = 0
a = 0

while sum <= num:
    a += 1
    sum += a

print(a-1)