import sys
import heapq
input = sys.stdin.readline

min = int(input())
schedule = []
score = 0
current = None

for i in range(min):
    work = list(map(int, input().split()))
# 새로 주어진 과제 없음
    if work[0] == 0:
        if current:
            current[1] -= 1
            if current[1] == 0:
                score += current[0]
                current = None

# not current - 현재 수행중인 과제 없음
# not schedule - 대기 중인 과제 없음
        if not current and schedule:
            current = schedule.pop()
# 과제 새로 주어짐
    else:
        if current:
            schedule.append(current)
        current = [work[1], work[2]-1]
# 과제 완료 - 점수 추가
        if current[1] == 0:
            score += current[0]
            current = None

# not current - 현재 수행중인 과제 없음
# not schedule - 대기 중인 과제 없음
        if not current and schedule:
            current = schedule.pop()

print(score)
