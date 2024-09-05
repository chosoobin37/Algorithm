import sys
from collections import Counter
input = sys.stdin.readline

words, length = map(int, input().split())
eng = []

for i in range(words):
    word = input().strip()
    if len(word) >= length:
        eng.append(word)

word_count = Counter(eng)

# 중복제거 하는 과정을 시간복잡도 줄이기 위해 list -> set -> list
# set -> 별도 알고리즘 필요 없이 자동으로 중복제거
result = list(set(eng))

# 자주 등장한 순, 길이가 긴 순, 사전 순 -> 우선순위 적용
result.sort(key=lambda x:(-word_count[x], -len(x), x))

for item in result:
    print(item)