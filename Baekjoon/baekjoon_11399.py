num = int(input())
arr = list(map(int, input().split()))

arr.sort()

sum=0

for i in range(num):
    sum += arr[i]*(num-i)
print(sum)