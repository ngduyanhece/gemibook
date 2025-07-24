# BookBot Tutorial: Build a Text Analysis Tool

Welcome to BookBot! This tutorial will guide you through building a Python program that analyzes novels and generates statistical reports on word and character usage. You'll learn to build a complete project from scratch while working with file I/O, data analysis, and command-line arguments.

## Learning Goals

- Practice building a full Python project from scratch
- Learn file handling and text processing
- Work with dictionaries and data analysis
- Understand command-line arguments
- Practice code organization across multiple files

## Prerequisites

- Basic Python knowledge (variables, functions, loops, dictionaries)
- Python 3.x installed on your system
- A text editor or IDE (VS Code recommended)

## Project Overview

BookBot will:

1. Read a text file (novel/book)
2. Count the total number of words
3. Count the frequency of each character
4. Generate a formatted report with statistics
5. Accept different book files via command-line arguments

---

## Step 1: Setting Up Your Environment

### Create the Project Structure

```bash
mkdir bookbot
cd bookbot
```

### Test Your Python Setup

Create a file called `main.py`:

```bash
touch main.py
```

Add this simple test code to `main.py`:

```python
print("Hello, BookBot!")
```

Run your program:

```bash
python3 main.py
```

If you see "Hello, BookBot!" printed to the console, you're ready to proceed!

---

## Step 2: Get Sample Book Data

We'll use "Frankenstein" by Mary Shelley from Project Gutenberg (public domain).

### Create Books Directory

```bash
mkdir books
```

### Download Frankenstein

Create `books/frankenstein.txt` and copy the text from:
https://www.gutenberg.org/cache/epub/41445/pg41445.txt

### Create .gitignore

Create a `.gitignore` file in your project root:

```
/books/
__pycache__/
*.pyc
```

This keeps large text files out of version control.

---

## Step 3: Reading Files

### Key Concepts

- **with statement**: Automatically handles file opening/closing
- **.read() method**: Reads entire file contents into a string

### Assignment

Replace your test code in `main.py` with:

1. **Create `get_book_text()` function** that:

   - Takes a filepath as parameter
   - Opens and reads the file
   - Returns the file contents as a string

2. **Create `main()` function** that:

   - Calls `get_book_text()` with the path to frankenstein.txt
   - Prints the entire book contents

3. **Call `main()`** at the bottom of the file

### Code Structure

```python
def get_book_text(path):
    # TODO: Implement file reading
    pass

def main():
    # TODO: Call get_book_text and print contents
    pass

if __name__ == "__main__":
    main()
```

### Test Your Code

Run `python3 main.py` - you should see the entire book printed to the console.

---

## Step 4: Count Words

Time for your first data analysis task!

### Key Concepts

- **.split() method**: Splits a string into a list of words
- **len() function**: Gets the length of a list

### Assignment

1. **Create `count_words()` function** that:

   - Takes text as a string parameter
   - Splits the text into words
   - Returns the number of words

2. **Update `main()`** to:
   - Get the book text
   - Count the words
   - Print: `{num_words} words found in the document`

### Test Your Code

You should see something like: `77963 words found in the document`

---

## Step 5: Refactor - Organize Your Code

Let's split our code into multiple files for better organization.

### Create stats.py

Move your word counting function to a new file called `stats.py`.

### Update main.py

Import the function:

```python
from stats import count_words
```

### File Structure

- `main.py`: Entry point and main logic
- `stats.py`: Text analysis functions

### Test Your Code

Make sure everything still works after the refactor.

---

## Step 6: Count Characters

The core feature of BookBot - character frequency analysis!

### Key Concepts

- **Dictionaries**: Store character -> count mappings
- **.lower() method**: Convert to lowercase
- **Dictionary operations**: `dict[key] = value`, `key in dict`

### Assignment

Add a new function to `stats.py`:

1. **Create `count_characters()` function** that:

   - Takes text as a string parameter
   - Converts all characters to lowercase
   - Counts frequency of each character (including spaces/symbols)
   - Returns a dictionary: `{'a': 1234, 'b': 567, ...}`

2. **Update `main()`** to:
   - Call the character counting function
   - Print the character dictionary

### Algorithm Hint

```python
def count_characters(text):
    char_count = {}
    for char in text.lower():
        # TODO: Count each character
    return char_count
```

---

## Step 7: Generate a Formatted Report

Transform your raw data into a beautiful report!

### Key Concepts

- **List of dictionaries**: `[{"char": "a", "num": 123}, ...]`
- **.sort() method**: Sort with custom key function
- **.isalpha() method**: Check if character is alphabetic

### Assignment

1. **Add `get_character_report()` to stats.py** that:

   - Takes the character count dictionary
   - Converts to list of dictionaries with "char" and "num" keys
   - Filters to alphabetic characters only
   - Sorts by count (highest first)
   - Returns the sorted list

2. **Update `main()`** to print a formatted report:

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
============= END ===============
```

### Sorting Example

```python
def sort_on(dict_item):
    return dict_item["num"]

char_list.sort(reverse=True, key=sort_on)
```

---

## Step 8: Command-Line Arguments

Make BookBot work with any book file!

### Key Concepts

- **sys.argv**: List of command-line arguments
- **sys.exit()**: Exit program with status code
- **Error handling**: Validate user input

### Assignment

1. **Import sys module** at the top of `main.py`

2. **Update `main()`** to:

   - Check if correct number of arguments provided
   - If not, print usage message and exit
   - Use the provided filepath instead of hardcoded path

3. **Usage message**: `Usage: python3 main.py <path_to_book>`

### Test Your Code

```bash
python3 main.py books/frankenstein.txt
```

---

## Testing Your Implementation

### Manual Tests

1. **Word Count**: Should be around 75,000-78,000 for Frankenstein
2. **Character Count**: 'e' should be the most frequent letter
3. **Error Handling**: Try running without arguments
4. **Different Files**: Test with a small text file

### Expected Output Format

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count ---------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
```

---

## Bonus Challenges

Once you complete the basic BookBot, try these extensions:

1. **Multiple File Support**: Analyze multiple books in one run
2. **JSON Export**: Save results to a JSON file
3. **Most Common Words**: Find the most frequent words (not just characters)
4. **Reading Level**: Calculate average word length
5. **GUI Version**: Create a simple graphical interface

---

## Final Project Structure

```
bookbot/
├── main.py          # Entry point and main logic
├── stats.py         # Text analysis functions
├── .gitignore       # Git ignore file
├── books/
│   └── frankenstein.txt
└── tests/
    ├── test_stats.py
    └── sample.txt
```

Congratulations! You've built a complete text analysis tool from scratch. This project demonstrates file I/O, data processing, code organization, and command-line interfaces - all essential skills for Python development.
