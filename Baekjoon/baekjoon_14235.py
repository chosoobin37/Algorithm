import sys
input = sys.stdin.readline

event = int(input())
gift = []

for i in range(event):
    visit = list(map(int, input().split()))
    if visit[0] == 0:
        if gift:
            print(max(gift))
            gift.remove(max(gift))
        else:
            print(-1)
    else:
        gift.extend(visit[1:])

# event = int(input())
# gift = []

# for i in range(event):
#     visit = list(map(int, input().split()))
#     if visit[0] == 0:
#         if gift:
#             print(max(gift))
#             gift.remove(max(gift))
#         else: 
#             print(-1)
#     else:
#         gift.extend(visit[1:]) # 첫번째 요소 제외 저장
