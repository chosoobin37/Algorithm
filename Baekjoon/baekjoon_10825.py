num = int(input())
score = []

for i in range(num):
    name, kor, eng, math = input().split()
    kor, eng, math = int(kor), int(eng), int(math)
    score.append((name, kor, eng, math))

score.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for item in score:
    print(item[0])