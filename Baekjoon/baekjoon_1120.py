import sys
input = sys.stdin.readline

a, b =input().split()

min_diff = len(a)

# B에서 A와 동일한 부분 찾기
for i in range(len(b)-len(a)+1):
# B 문자열 중에서 A크기만큼을 덩어리로 비교
# B에서 A길이만큼씩 비교
  sub_b = b[i:i+len(a)]

# 차이점 0으로 기본 설정 
  diff = 0
  # A의 문자열 크기만큼
  for j in range(len(a)):
    # A의 j번째 문자열과 B에서 추출한 문자열의
    # j번째 문자열 비교 
    # 다를 경우 차이가 생긴 거니 +1
    if a[j] != sub_b[j]:
      diff += 1

  min_diff = min(min_diff, diff)

print(min_diff)