goals = int(input())
team1_time = 0
team2_time = 0
last_time = 0
team1_score = 0
team2_score = 0

for i in range(goals):
    team, time = input().split()
    minute, second = map(int, time.split(":"))
    current_time = minute*60 + second

    if team1_score > team2_score:
        team1_time += current_time - last_time
    elif team2_score > team1_score:
        team2_time += current_time - last_time

    if team == '1':
        team1_score += 1
    else:
        team2_score += 1

    last_time = current_time

if team1_score > team2_score:
    team1_time += 48*60 - last_time
elif team2_score > team1_score:
    team2_time += 48*60 - last_time

print(f"{team1_time // 60:02}:{team1_time % 60:02}")
print(f"{team2_time // 60:02}:{team2_time % 60:02}")
