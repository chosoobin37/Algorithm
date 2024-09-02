import sys
input = sys.stdin.readline

num = int(input())

if num > 0:
  arr = list(map(int, input().split()))

  unique = []

  for i in arr:
    if i not in unique:
      unique.append(i)

  unique.sort()

print(" ".join(map(str, unique)))