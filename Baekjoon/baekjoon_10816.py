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