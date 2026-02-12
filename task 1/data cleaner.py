# Data Cleaner
names = [" Alice ", "bob", " CHARLIE "]
# remove extra spaces and convert to lowercase
clean_names = [name.strip().lower() for name in names]
print("Cleaned names:")
print(clean_names)
