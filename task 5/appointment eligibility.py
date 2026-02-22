def appointment_eligibility(age):
    if age >= 18:
        eligibility = "Eligible"
    else:
        eligibility = "Not Eligible"
    print("Age:", age)
    print("Eligibility status:", eligibility)
appointment_eligibility(21)