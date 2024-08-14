import sys
import heapq
input = sys.stdin.readline

min = int(input())
schedule = [] # 대기 중인 과제가 여러 개 있을 수 있어서 []로 선언
score = 0
current = None # 현재 작업중인 과제는 오직 하나, None은 현재 작업중인 과제 없음 의미

for i in range(min):
    work = list(map(int, input().split()))
# 새로 주어진 과제 없음
    if work[0] == 0:
        if current:
            current[1] -= 1
            if current[1] == 0:
                score += current[0]
                current = None # 과제 완료 시 점수 추가하고 작업중인 과제 초기화

# not current - 현재 수행중인 과제 없음
# not schedule - 대기 중인 과제 없음
# 둘 다 없는 경우 가장 최근에 추가된 과제 가져옴(대기 중인 과제들 중)
        if not current and schedule:
            current = schedule.pop()

# 과제 새로 주어짐
    else:
        # 과제가 새로 주어졌는데 지금 수행중인 과제가 있는 경우
        if current:
            # 현재 과제를 대기 목록에 추기
            schedule.append(current)
            # 새 과제를 현재 과제로 반영하고 시간 -1(분)
        current = [work[1], work[2]-1]

# 새로 추가된 과제가 바로 완료된 경우
        if current[1] == 0:
            # 점수 반영 후
            score += current[0]
            # 현재 작업중인 과제 초기화
            current = None

# 현재 진행중인 과제도 없고 대기 중인 과제 아직 안 불러온 상태
# 가장 최근에 추가된 과제 불러옴 (대기 중이던 과제들 중에서)
        if not current and schedule:
            current = schedule.pop()

print(score)
