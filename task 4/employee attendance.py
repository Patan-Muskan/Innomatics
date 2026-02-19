def attendance_check(attendance):
    present = 0
    for day in attendance:
        if day == "P":
            present += 1
    percentage = (present / len(attendance)) * 100
    if percentage >= 75:
        return "Eligible"
    else:
        return "Not Eligible"
attendance = ["P", "A", "P", "P", "A", "P", "P", "A"]
print(attendance_check(attendance))