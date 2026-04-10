with open("inputs.txt", "r") as f:
    text = f.read().lower()
words = text.split()
word_counts = {}
total_length = 0
longest_word = ""

for word in words:
    if word == "":continue

    total_length += 1
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


    if len(word) > len(longest_word):
        longest_word = word


reversed_word = longest_word[::-1]
print(words)
print("Total word count:", total_length)
print("Longest word:", longest_word)
print("Reversed word:", reversed_word)
print("\nRepeated words:")
for wordss in word_counts:
    if word_counts[wordss] > 1:
        print(wordss ,":", word_counts[wordss])
