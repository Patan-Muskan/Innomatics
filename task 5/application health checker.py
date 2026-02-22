def application_health_checker(errors):
    if errors == 0:
        status = "Healthy"
    elif errors <= 5:
        status = "Minor Issues"
    else:
        status = "Critical Issues"
    print("Error count:", errors)
    print("System Status:", status)
application_health_checker(7)
