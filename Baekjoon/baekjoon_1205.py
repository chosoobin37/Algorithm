import sys
input = sys.stdin.readline

ranks, ts_score, max_rank_size = map(int, input().split())

if ranks > 0:
    current_rank = list(map(int, input().split()))
else:
    current_rank = []

current_rank.append(ts_score)
current_rank.sort(reverse=True)

if len(current_rank) > max_rank_size:
    if ts_score == current_rank[-1]:
        print(-1)
    else:
        # 가장 낮은 점수 pop해서 등록 가능한 랭크 크기 유지
        current_rank.pop()
        print(current_rank.index(ts_score) + 1)
else:
    print(current_rank.index(ts_score) + 1)