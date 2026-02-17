text = "Buy mobile phone buy phone online"
# convert to lower case
text = text.lower()
# remove punctuation
for char in ",.!?":
    text = text.replace(char, "")
# split into words
words = text.split()
# count frequency
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
result = {}
for word, count in freq.items():
    if count > 1:
        result[word] = count
print(result)
