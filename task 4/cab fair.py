def fare(km, peak):
    cost = 50 + (km * 12)
    if peak:
        cost*= 1.25
    return cost
while True:
    distance = float(input("Enter the distance traveled in km: "))
    peak_time = input("Is it peak time? (yes/no): ").lower() 
    total = fare(distance, peak_time)
    print("Total fare:", total)
    again = input("Do you want to calculate fare for another trip? (yes/no): ").lower()
    if again != "yes":
        break
    