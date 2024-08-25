import sys
from collections import deque
input = sys.stdin.read

data = input().splitlines()

repeat = int(data[0])
number = deque()

for i in range(1, repeat+1):
    order = data[i].split()

    if order[0] == 'push':
        number.append(int(order[1]))
    elif order[0] == 'pop':
        print(number.popleft() if number else -1)
    elif order[0] == 'size':
        print(len(number))
    elif order[0] == 'empty':
        print(0 if number else 1)
    elif order[0] == 'front':
        print(number[0] if number else -1)
    elif order[0] == 'back':
        print(number[-1] if number else -1)