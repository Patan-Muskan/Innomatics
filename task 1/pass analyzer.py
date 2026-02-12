# Pass/Fail Analyzer
marks = [45, 78, 90, 33, 60]
pass_count = 0
fail_count = 0
for i in marks:
    if i >= 50:
        print(f"Marks: {i} - Pass")
        pass_count += 1
    else:
        print(f"Marks: {i} - Fail")
        fail_count += 1
print(f"\nTotal number of students passed: {pass_count}")
print(f"Total number of students failed: {fail_count}")
