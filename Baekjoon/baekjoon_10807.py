num = int(input())
arr = list(map(int, input().split()))
find = int(input())

count = 0

for i in range(num):
    if find == arr[i]:
        count += 1

print(count)