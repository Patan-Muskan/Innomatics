def rainfall_checker(rainfall_list, required_level):
    total_rainfall = 0
    for rainfall in rainfall_list:
        total_rainfall += rainfall
    average_rainfall = total_rainfall / len(rainfall_list)
    if average_rainfall >= required_level:
        status = "Adequate Rainfall"
    else:
        status = "Inadequate Rainfall"
    print("Average Rainfall:", average_rainfall)
    print("Rainfall Status:", status)
rainfall = [70, 75, 80, 63]
rainfall_checker(rainfall, 70)