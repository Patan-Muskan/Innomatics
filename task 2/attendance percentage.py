attendance = ["P", "P", "A", "P", "P"]
present = 0
# loop to count present days
for day in attendance:
    if day == "P":
        present += 1
# calculate attendance percentage
percentage = (present / len(attendance)) * 100
# print attendance percentage   
print("attendance percentage:", percentage)