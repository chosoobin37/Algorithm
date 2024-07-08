count, num=map(int, input().split())
arr = list(map(int, input().split()))

save = []

for i in range(count):
    if arr[i] < num:
        save.append(arr[i])

print(*save)