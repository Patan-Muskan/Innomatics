sales = [1200, 1500, 900, 2200, 1400, 3000]
# average daily sales
avg = sum(sales) / len(sales)
# sales more than 30% above average
threshold = avg * 1.29
for i, value in enumerate(sales, start=1):
    if value > threshold:
        print(f"Day {i}: {value}")