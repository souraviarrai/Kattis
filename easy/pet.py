score = 0
winner = 0

for contestant in range(5):
    grade = [int(x) for x in input().split()]
    total = sum(grade)
    if total > score:
        winner = (contestant+1)
        score = total
print(f'{winner} {score}')
