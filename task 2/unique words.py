# take input
Sentence = input("Enter a sentence: ")
# split and find unique words
words = Sentence.split()
unique_words = set(words)
# print unique words and count
print(" Unique words count:", len(unique_words))
print(" Unique words:", unique_words)