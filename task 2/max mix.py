numbers = list(map(int, input("enter the list elements (space-separated): ").split()))
# initialize max and min values
max_val = numbers[0]
min_val = numbers[0]
# loop to find max and min
for n in numbers:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n
#print the max and min values
print("Maximum value:", max_val)
print("Minimum value:", min_val)
