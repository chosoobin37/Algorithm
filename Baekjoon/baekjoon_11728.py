import sys
input = sys.stdin.readline

a, b = map(int, input().split())

arra = list(map(int, input().strip().split()))
arrb = list(map(int, input().strip().split()))

arr = arra + arrb
arr.sort()

print(" ".join(map(str, arr)))
