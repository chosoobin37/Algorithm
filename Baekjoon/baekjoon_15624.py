import sys

inpit = sys.stdin.readline

num = int(input())

a, b = 0, 1

for i in range(2, num+1):
    a, b = b, (a+b) % 1000000007

print(b)

# import sys
# input = sys.stdin.readline

# num = int(input())
# arr = []

# arr.append(0)
# arr.append(1)

# for i in range(2, num+1):
#     i = arr[i-2] + arr[i-1]
#     arr.append(i)


# print((arr[num] % 1000000007))