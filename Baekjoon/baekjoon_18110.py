import sys
import math

input = sys.stdin.readline

def new_round(n):
    return math.floor(n+0.5)

person = int(input())
levels = []

if person > 0:
    for i in range(person):
        suggest = int(input())
        levels.append(suggest)

    levels.sort()

    new_person = new_round(person * 0.15)

    if new_person > 0:
        levels = levels[new_person:-new_person]

    if len(levels) > 0:
        level = new_round(sum(levels)/len(levels))
    else: 
        level = 0
        
else:
    level = 0

print(level)