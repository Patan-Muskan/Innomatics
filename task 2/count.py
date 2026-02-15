prices = [450, 1200, 899, 1500, 300]
count = 0
# loop to count products above 1000
for p in prices:
    if p > 1000:
        count += 1
# print the count of products above 1000
print("Products above 1000:", count)