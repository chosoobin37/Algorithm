import sys
from collections import Counter
input = sys.stdin.readline

get = int(input())
get_card = list(map(int, input().split()))

find = int(input())
find_card = list(map(int, input().split()))

count_card = Counter(get_card)

result = []
for card in find_card:
    result.append(str(count_card[card]))

print(" ".join(result))

# import sys
# input = sys.stdin.readline

# # N (숫자 카드의 개수) 입력
# get = int(input())

# # 숫자 카드에 적힌 숫자들 입력
# get_card = list(map(int, input().split()))

# # M (찾고자 하는 카드의 개수) 입력
# find = int(input())

# # 찾고자 하는 카드의 숫자들 입력
# find_card = list(map(int, input().split()))

# # 숫자 카드의 숫자 개수를 세기 위한 딕셔너리 초기화
# count_card = {}

# # get_card 리스트에 있는 각 숫자의 개수를 미리 셈
# for card in get_card:
#     if card in count_card:
#         count_card[card] += 1  # 이미 존재하는 숫자라면 1 증가
#     else:
#         count_card[card] = 1   # 처음 등장하는 숫자는 1로 초기화

# # find_card 리스트에서 각 숫자가 몇 개 있는지 찾기
# result = []
# for card in find_card:
#     # count_card에서 찾고자 하는 카드의 개수를 가져옴. 없으면 0을 반환
#     result.append(str(count_card.get(card, 0)))

# # 결과 출력, 리스트를 공백으로 구분하여 출력
# print(" ".join(result))