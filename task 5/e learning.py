def eligibility(attendance_list):
    total_classes=len(attendance_list)
    attended_classes=0
    for day in attendance_list:
        attended_classes+=day
        percentage=(attended_classes/total_classes)*100
    if percentage>=75:
        status="Eligible"
    else:
        status="Not Eligible"
    print("Attendance Percentage:", percentage)
    print("Eligibility:", status)
eligibility([1, 1, 1, 0, 1])