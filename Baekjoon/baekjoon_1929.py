import sys
input = sys.stdin.readline

m, n = map(int, input().split())

is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, n+1, i):
            is_prime[j] = False

for i in range(m, n+1):
    if is_prime[i]:
        print(i)

# 1.	첫 번째 반복문 (for i in range(2, int(n**0.5) + 1)):
# •	i는 2부터 시작하여 n의 제곱근까지 증가합니다.
# •	n의 제곱근까지만 확인하는 이유는, 예를 들어 100이라는 숫자가 소수가 아니라면 10 이하의 어떤 숫자로 나눌 수 있어야 하기 때문입니다. 
# • 즉, 어떤 수의 약수는 반드시 제곱근 이하에서 등장합니다.
# 2.	두 번째 반복문 (for j in range(i * i, n + 1, i)):
# •	i가 소수인 경우(is_prime[i] == True), i의 배수들은 모두 소수가 아닙니다.
# •	예를 들어, i = 2일 때, 4, 6, 8, 10, …은 모두 2의 배수이므로 소수가 아니며 False로 설정됩니다.
# •	j는 i*i부터 n까지 i씩 증가합니다. i*i부터 시작하는 이유는, 그 이전의 배수들은 이미 소수 여부가 판단된 상태이기 때문입니다.
# 3.	결과:
# •	이 반복이 끝나면, 소수가 아닌 모든 수는 False로 설정되고, True로 남아 있는 숫자들은 모두 소수입니다.