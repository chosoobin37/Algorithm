import sys
import math

input = sys.stdin.readline

repeat = int(input())
gcd_sum = []

for i in range(repeat):
    numbers = list(map(int, input().split()))
    n = numbers[0]
    nums = numbers[1:]

    total_gcd_sum = 0

    for i in range(n):
        for j in range(i+1, n):
            total_gcd_sum += math.gcd(nums[i], nums[j])
    
    gcd_sum.append(total_gcd_sum)

for item in gcd_sum:
    print(item)