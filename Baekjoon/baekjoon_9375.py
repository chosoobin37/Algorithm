# from collections import Counter

# num = int(input())
# arr = []

# mean = 0
# mid =0
# mode = 0
# area = 0

# for i in range(num):
#     number = int(input())
#     arr.append((number))

# sum = 0
# for i in range(num):
#     sum += arr[i]
# mean = int(round((sum/num), 0))

# sorted_arr = sorted(arr)
# mid = sorted_arr[int((num/2))]

# counter = Counter(arr)
# max_count = max(counter.values())
# modes = [k for k, v in counter.items() if v == max_count]
# modes.sort()
# if len(modes) > 1:
#     mode = modes[1]
# else:
#     mode = modes[0]

# area = max(arr) - min(arr)

# print(mean)
# print(mid)
# print(mode)
# print(area)

import sys
from collections import defaultdict

input = sys.stdin.readline

num = int(input())
arr = []

sum = 0
frequency = defaultdict(int)
max_freq = 0

for i in range(num):
    number = int(input())
    arr.append(number)
    sum += number
    frequency[number] += 1
    if frequency[number] > max_freq:
        max_freq = frequency[number]

mean = int(round(sum/num))

arr.sort()
mid = arr[num//2]

modes = []
for key, value in frequency.items():
    if value == max_freq:
        modes.append(key)
modes.sort()

if len(modes) > 1:
    mode = modes[1]
else:
    mode = modes[0]

area = arr[-1] - arr[0]

print(mean)
print(mid)
print(mode)
print(area)