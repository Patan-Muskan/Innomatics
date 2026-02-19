def result(marks):
    total = 0
    for m in marks :
        total += m
    average = total / len(marks)
    if average >= 50:
        return "Pass"
    else:
        return "Fail"
marks = [60, 35, 79, 45]
print(result(marks))