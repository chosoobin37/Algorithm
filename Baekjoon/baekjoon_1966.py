import sys
from collections import deque

input = sys.stdin.readline

test = int(input())

for i in range(test):
    file, find_file = map(int, input().split())
    file_importance = list(map(int, input().split()))

    # queue = deque((file_importance[i], i) for i in range(file))
    queue = deque()
    for i in range(file):
        queue.append((file_importance[i], i))

    print_order = 0

    # queue에 문서가 남아있는 한
    while queue:
        # 가장 앞에 있는 문서 꺼내서 current에 저장
        current = queue.popleft()
        # current[0] - 현재 문서의 중요도(맨 앞에 있는 문서의 중요도)
        # q[0] - 큐에 남아있는 문서들의 중요도
        # 현재 문서보다 높은 중요도를 가진 문서가 하나라도 queue에 남아있는지 확인
        if any(current[0] <q[0] for q in queue):
            # 만약 남은 문서가 현재 문서보다 중요도가 높을 경우 현재 문서 queue 맨뒤로
            queue.append(current)
        # 남은 문서들 중 현재 문서보다 중요도가 높은 문서가 없을 경우
        else:
            print_order += 1
            # 현재 문서가 내가 찾고자하는 문서인 find_file일 경우
            if current[1] == find_file:
                print(print_order)
                break


