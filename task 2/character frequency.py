text = "ppthon"
frequency = {}
# loop to count frequency of each character
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
# print character frequency
print(frequency)