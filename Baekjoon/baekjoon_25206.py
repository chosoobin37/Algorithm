count = 20

grade_to_score = {
    'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}

total_score = 0.0
total_credit = 0.0

for i in range(count):
    chihoon = input().split()
    credit = float(chihoon[1])
    grade = chihoon[2]

    if grade == "P":
        continue
    
    total_score += grade_to_score[grade]*credit
    total_credit += credit

if total_credit > 0:
    gpa = total_score/total_credit
else:
    gpa = 0.0

print(gpa)