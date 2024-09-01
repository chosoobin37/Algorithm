import sys
input = sys.stdin.readline

num = int(input())
arr = []

for i in range(num):
    number = int(input())
    arr.append(number)

arr.sort()

for item in arr:
    print(item)