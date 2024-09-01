import sys
input = sys.stdin.readline

exist = int(input())
exist_nums = set(map(int, input().split()))

find = int(input())
find_nums = list(map(int, input().split()))

result = []

for num in find_nums:
    if num in exist_nums:
        result.append("1")
    else:
        result.append("0")

print(" ".join(result))