# import section
from collections import Counter

# Initialization section

frequency_dictionary = {}

paragraph = ""

common_words = [
    "the", "be", "to", "of", "an", "a", "in", "that", "have", "I", "it",
    "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his",
    "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one",
    "all", "would", "their", "there", "what", "so", "up", "out", "if", "about",
    "who", "get", "which", "go", "me", "when", "make", "can", "like", "no", "just", "him",
    "take", "into", "year", "your", "good", "some", "could", "them", "see", "other",
    "than", "then", "now", "look", "only", "come", "its", "over", "think", "also",
    "back", "after", "use", "two", "how", "our", "first", "well", "way", "even", "new",
    "want", "because", "any", "these", "give", "day", "most", "us", "long", "tool", "before",
    "and", "was", "company", "focus", "is", "are", "had", "more", "saying", "years",
    "days", "people", "has", "those", "thing", "told", "wrote", "really", "things"
]

# Processing section

text_file = open("input.txt")

for line in text_file:
    paragraph += line.lower()

text_file.close()

paragraph_array = paragraph.split()

for word in paragraph_array:
    # Easier way of either adding a key/modifying a key's value conditionally
    frequency = frequency_dictionary.setdefault(word, 1)

    new_frequency = frequency + 1
    frequency_dictionary[word] = new_frequency

for comword in common_words:
    status = frequency_dictionary.get(comword, -999)

    if status > 0: 
        # common word has been found in dictionary, 
        # must remove it to focus on the key words
        frequency_dictionary.pop(comword)

# sort the frequencies
sorted_frequencies = dict(Counter(frequency_dictionary).most_common())

words = list(sorted_frequencies.keys())
frequencies = list(sorted_frequencies.values())

# print the 10 most frequent words from your paragraph

for index in range(10):
    print(f"{words[index]} appeared {frequencies[index]} times")