import sys

num = int(input())
success = []

for i in range(num):
    level = int(input())
    success.append(level)

count = 0

for i in range(num-1, 0, -1):
    if success[i] <= success[i-1]:
        count += success[i-1] - success[i] + 1
        success[i-1] = success[i] -1

print(count)