num = int(input())
turn = list(map(int, input().split()))

balloons = [(i+1, turn[i]) for i in range(num)]
# [(1,3), (2, 2), (3, 1), (4, -3), (5 -1)] 형식으로 저장
bomb = []

ci = 0

while balloons:
    balloon = balloons.pop(ci)
    bomb.append(balloon[0])

    if not balloons:
        break

    move = balloon[1]
    if move > 0:
        ci = (ci + (move-1)) % len(balloons)
    else:
        ci = (ci + move) % len(balloons)

print(" ".join(map(str, bomb)))