''' Use a lambda function to calculate grades for a list of scores.
Criteria:
A > 90, B > 80, c < 80'''
scores = [85, 92, 78, 88, 95, 72, 60, 100]

grades = list(map(lambda score: 'A' if score > 90 else 'B' if score > 80 else 'C', scores))

print(grades)
