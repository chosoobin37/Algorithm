import math

son = 0
mom = 0

s1, m1 = map(int, input().split())
s2, m2 = map(int, input().split())

son = s1*m2 + s2*m1
mom = m1*m2

gcd = math.gcd(son, mom)
# son을 최대공약수로 나눔
son //= gcd
# mom을 최대공약수로 나눔
mom //= gcd
# 최대공약수로 나누면서 기약분수화

print(son, mom)