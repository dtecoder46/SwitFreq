# SwitFreq
A word frequency program made in Swift

# How to Install

1. Clone the repository on your IDE
2. Install Swift on your operating system
- [Install page for Swift](https://www.swift.org/install/macos/)
3. Run Swift
~~~sh
swift main.swift
~~~

# How it Works

Concepts used
- I/O
- String replace and split
- Dictionary
- For loop
- Conditional logic
- Increment operator

1. Ask the user for paragraph input
2. Replace all junk characters ! @ # $ % ^ & * ( ) - + = { } [ ] | \ ' ' " " : ; ? / . > < , ~ ` in the text with an empty string 
3. Split the text by spaces to make an array of words
4. Declare a frequency dictionary
5. For each item in the array of words
    1. If the word is a common word (a, an, the, it, etc.)
        1. Do nothing
    2. Else if the item is a key in the dictionary
        1. Increment it's frequency by 1
    3. Else
        1. Declare the word key with a value of 16. For each key in the dictionary
    1. Print each word key along with it's frequency