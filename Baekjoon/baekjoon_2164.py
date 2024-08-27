import sys
from collections import deque
input = sys.stdin.readline

num = int(input())
cards = deque()

for i in range(num):
    cards.append(i+1)

for i in range(num-1):
    cards.popleft()
    cards.append(cards.popleft())

for item in cards:
    print(item)