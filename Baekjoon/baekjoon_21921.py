day, sequence = map(int, input().split())
visit = list(map(int, input().split()))

max_visit = sum(visit[:sequence])
sum_visit = max_visit
count = 1

for i in range(sequence, day):
    sum_visit += visit[i] - visit[i-sequence]
    if sum_visit > max_visit:
        max_visit = sum_visit
        count = 1
    elif sum_visit == max_visit:
        count += 1

if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(count)