import sys
input = sys.stdin.readline

test = int(input())

for i in range(test):
    exist = int(input())
    exist_nums = set(map(int, input().split()))

    find = int(input())
    find_nums = list(map(int, input().split()))

    for num in find_nums:
        if num in exist_nums:
            print(1)
        else:
            print(0)