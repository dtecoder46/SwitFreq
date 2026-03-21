# RFreq
A word frequency program made in Rust

# Credits
1. [w3Schools Python](w3schools.com/python)
2. [Wikipedia most common English words](https://en.wikipedia.org/wiki/Most_common_words_in_English)
3. [GeeksforGeeks sort Python dictionar descending](https://www.geeksforgeeks.org/python/sort-dictionary-by-value-python-descending/)

# How to Install

1. Clone the repository on your IDE
2. [Install Python](https://www.python.org/)
3. Run the file
~~~bash
python3 main.py
~~~

# How it Works

Concepts used
- Print
- File handling
- String replace and split
- Dictionary
- For loop
- Conditional logic
- Increment operator

1. Get input from text file
2. Split the text by spaces to make an array of words
3. Declare a frequency dictionary
4. For each item in the array of words
    1. If the item is a key in the dictionary
        1. Increment it's frequency by 1
    2. Else
        1. Declare the word key with a value of 1 
5. For each common word in the common words list
    1. If the common word is found in the frequency dictionary
        1. Remove it from the dictionary
6. Sort the frequency dictionary
7. Get the words and frequencies as arrays
8. Loop 10 times
    1. Print out the word and frequency at the index

# Instructions
Before pasting your text, run it through a punctuation remover. I tried removing punctuation and many other junk characters via Python's replace() and strip() methods, but both failed to actually remove the characters.

Then paste your text into input.txt and run the command. After that, let the program do its magic!