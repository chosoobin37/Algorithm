import sys
from collections import Counter
input = sys.stdin.readline

num = int(input())
numbers = []

for i in range(num):
    number = int(input())
    numbers.append(number)

count_numbers = Counter(numbers)

max_count = max(count_numbers.values())

# common = [key for key, value in count_numbers.items() if value == max_count]
common = []
for key, value in count_numbers.items():
    if value == max_count:
        common.append(key)

print(min(common))