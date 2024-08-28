import sys
input = sys.stdin.readline

exist = int(input())
exist_nums = set(map(int, input().split()))

find = int(input())
find_nums = set(map(int, input().split()))

for num in find_nums:
    if num in exist_nums:
        print(1)
    else:
        print(0)