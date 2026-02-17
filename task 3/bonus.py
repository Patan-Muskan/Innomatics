employees = {
"Ravi": 92,
"Anita": 88,
"Kiran": 92,
"Suresh": 85
}
# find highest performance score
highest_score = max(employees.values())
# see who has same highest score
top_employees = []
for name, score in employees.items():
    if score == highest_score:
        top_employees.append(name)
print("Top Performers eligible for bonus:",", ".join(top_employees), "(Score:", highest_score, ")")