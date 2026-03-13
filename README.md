# RFreq
A word frequency program made in Rust

# Credits
1. Gemini
    1. [Gemini Read from File](https://www.google.com/search?q=rust+file+handling&oq=rust+file+h&gs_lcrp=EgZjaHJvbWUqDAgBEAAYFBiHAhiABDIGCAAQRRg5MgwIARAAGBQYhwIYgAQyBwgCEAAYgAQyDAgDEAAYFBiHAhiABDIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBCDMwMTVqMGo5qAIGsAIB8QWfhw82WpewDg&sourceid=chrome&ie=UTF-8)
    2. [Gemini Substring Replacement](https://www.google.com/search?q=rust+string+replace&oq=rust+string+repl&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBwgBEAAYgAQyBggCEEUYOTIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIICAgQABgWGB4yCAgJEAAYFhge0gEIMzA3NmowajSoAgCwAgE&sourceid=chrome&ie=UTF-8)
2. [w3Schools Rust](https://www.w3schools.com/rust/index.php)

# How to Install

1. Clone the repository on your IDE
2. [Install Rust for your OS](https://rust-lang.org/learn/get-started/)
3. Run the file

# How it Works

Concepts used
- Print
- File handling
- String replace and split
- Dictionary
- For loop
- Conditional logic
- Increment operator

1. Ask the user for paragraph input
2. Create an array containing the characters
> ! @ # $ % ^ & * ( ) - + = { } [ ] | \ ' ' " " : ; ? / . > < , ~ `
3. For each character in the junk array, replace the character with an empty string 
4. Split the text by spaces to make an array of words
5. Declare a frequency dictionary
6. For each item in the array of words
    1. If the word is a common word (a, an, the, it, etc.)
        1. Do nothing
    2. Else if the item is a key in the dictionary
        1. Increment it's frequency by 1
    3. Else
        1. Declare the word key with a value of 16. For each key in the dictionary
    1. Print each word key along with it's frequency