# 📚 GemiBook: BookBot Tutorial with Gemini CLI

A comprehensive Python tutorial project that demonstrates how to build a text analysis tool (BookBot) while learning to code collaboratively with Gemini CLI. This project showcases the power of AI-assisted development through hands-on learning.

## 🎯 Project Overview

GemiBook is an educational project that teaches you to:

- **Build a complete Python application** from scratch (BookBot - a text analysis tool)
- **Learn AI-assisted development** using Gemini CLI as your coding companion
- **Master essential Python concepts** including file I/O, data structures, and command-line interfaces
- **Practice test-driven development** with comprehensive test suites
- **Experience modern development workflows** with proper project structure and version control

## 🤖 What is BookBot?

BookBot is a Python program that analyzes novels and generates statistical reports on word and character usage. It demonstrates practical programming concepts while building something genuinely useful.

**BookBot Features:**
- 📖 Read and analyze text files (books, documents, etc.)
- 🔢 Count total words in any document
- 📊 Analyze character frequency with detailed statistics
- 📄 Generate beautifully formatted reports
- 🎯 Handle command-line arguments for different input files
- ✅ Comprehensive test coverage for all functionality

## 🚀 Quick Start Guide

### Prerequisites

1. **Python 3.x** installed on your system
2. **Node.js 20+** or **Homebrew** for Gemini CLI installation
3. **A text editor** or IDE (VS Code recommended)

### Step 1: Clone and Setup

```bash
git clone <your-repo-url>
cd gemibook
```

### Step 2: Install Gemini CLI

Follow the detailed installation guide in [`GEMINI_CLI_SETUP.md`](GEMINI_CLI_SETUP.md):

**Option A: With Node.js**
```bash
npm install -g @google/gemini-cli
```

**Option B: With Homebrew**
```bash
brew install gemini-cli
```

### Step 3: Configure Authentication

Set up your API key (choose one):

```bash
# Gemini API (recommended for learning)
export GEMINI_API_KEY="your-api-key-here"

# OR Vertex AI (for enterprise)
export GOOGLE_API_KEY="your-api-key-here"
export GOOGLE_GENAI_USE_VERTEXAI=true
```

### Step 4: Start Your AI-Assisted Learning Journey

```bash
cd gemibook
gemini
```

![Gemini CLI in Action](asset/gemini-screenshot.png)

*The Gemini CLI provides an interactive environment where you can ask questions, get code help, and learn step-by-step while building your BookBot.*

## 🎓 Learning Path with Gemini CLI

### Phase 1: Project Setup and Understanding (5-10 minutes)

Start your Gemini CLI session and begin with these prompts:

```
> I'm starting the BookBot tutorial. Can you help me understand the project structure and what we'll be building?

> Explain the learning objectives of this BookBot project and how each step builds on the previous one.

> What are the key Python concepts I'll learn while building BookBot?
```

### Phase 2: Step-by-Step Implementation (30-45 minutes)

Work through [`BOOKBOT_TUTORIAL.md`](BOOKBOT_TUTORIAL.md) with Gemini CLI assistance:

**Step 1 - Environment Setup:**
```
> Help me set up the basic Python environment and create the initial main.py file for BookBot

> I need to create a simple "Hello BookBot" program to test my Python setup. Show me the code and explain what it does.
```

**Step 2 - File Reading:**
```
> I need to implement the get_book_text() function that reads a file and returns its contents. Help me write this using Python's 'with' statement.

> My file reading isn't working. Here's my code: [paste your code]. Can you debug this and explain the fix?
```

**Step 3 - Word Counting:**
```
> Help me implement the count_words() function that takes text and returns the number of words using the .split() method.

> I want to test my word counting function. Can you help me write some test cases to verify it works correctly?
```

**Step 4 - Code Organization:**
```
> I need to refactor my code by moving the word counting function to a new stats.py file. Help me organize this properly and set up the imports.

> Explain the benefits of splitting code across multiple files and how Python imports work.
```

**Step 5 - Character Analysis:**
```
> Help me implement the count_characters() function that counts the frequency of each character in the text using a dictionary.

> I'm getting confused with dictionary operations in Python. Can you explain how to count characters step by step?
```

**Step 6 - Data Processing:**
```
> I need to create a get_character_report() function that converts my character dictionary to a sorted list. Help me implement this with proper sorting.

> My character sorting isn't working correctly. Here's my code: [paste code]. Can you fix this and explain the sorting logic?
```

**Step 7 - Report Generation:**
```
> Help me format the output into a beautiful report that matches the expected format in the tutorial.

> I want to add some polish to my report formatting. Can you suggest improvements and show me how to implement them?
```

**Step 8 - Command Line Arguments:**
```
> I need to add command-line argument support using sys.argv. Help me implement proper argument handling with error messages.

> My argument parsing has bugs. Here's the error I'm getting: [paste error]. Can you help me fix this?
```

### Phase 3: Testing and Validation (10-15 minutes)

```
> I want to run the test suite to validate my implementation. Help me understand the test files and run them properly.

> Some of my tests are failing. Here's the output: [paste test output]. Can you help me debug and fix the issues?

> Can you help me add additional test cases to make my BookBot more robust?
```

### Phase 4: Extensions and Improvements (Optional - 15-30 minutes)

```
> My basic BookBot is working! Can you suggest some interesting extensions or improvements I could add?

> I want to add [specific feature like JSON export/GUI/multiple file support]. Help me design and implement this enhancement.

> Can you help me optimize my BookBot for better performance with large files?
```

## 📁 Project Structure

```
gemibook/
├── README.md                 # This file - project overview and guide
├── BOOKBOT_TUTORIAL.md       # Detailed step-by-step tutorial
├── GEMINI_CLI_SETUP.md       # Gemini CLI installation guide
├── .gitignore               # Git ignore rules
├── skeleton/                # Starter code templates
│   ├── main.py             # Main program skeleton with TODOs
│   └── stats.py            # Statistics functions skeleton
├── tests/                  # Comprehensive test suites
│   ├── test_stats.py       # Unit tests for statistics functions
│   └── test_main.py        # Integration tests for main program
└── books/                  # Sample book data for testing
    └── sample.txt          # Sample text from Frankenstein
```

## 🎯 Learning Outcomes

By completing this tutorial with Gemini CLI, you will:

- ✅ **Master Python fundamentals**: File I/O, dictionaries, functions, imports
- ✅ **Understand data analysis**: Text processing, character frequency, sorting
- ✅ **Learn project organization**: Multi-file projects, proper code structure
- ✅ **Practice testing**: Unit tests, integration tests, test-driven development
- ✅ **Experience AI collaboration**: How to effectively use AI assistants for coding
- ✅ **Build something real**: A functional text analysis tool you can use

## 🧪 Testing Your Implementation

The project includes comprehensive test suites to validate your work:

```bash
# Test individual functions
python3 tests/test_stats.py

# Test main program functionality  
python3 tests/test_main.py

# Test with sample data
python3 skeleton/main.py books/sample.txt
```

## 🎉 Expected Final Output

When your BookBot is complete, it should produce output like this:

```
============ BOOKBOT ============
Analyzing book found at books/sample.txt...
----------- Word Count ----------
Found 547 total words
--------- Character Count -------
e: 95
t: 73
a: 69
r: 56
n: 55
o: 54
i: 52
...
============= END ===============
```

## 🤝 AI-Assisted Development Tips

**Effective Prompting Strategies:**
- Be specific about what you're trying to implement
- Share error messages and code snippets when debugging
- Ask for explanations, not just solutions
- Request test cases and validation approaches
- Seek code review and improvement suggestions

**Learning Best Practices:**
- Work through each step methodically
- Test frequently as you build
- Ask "why" questions to deepen understanding
- Experiment with variations and improvements
- Use Gemini CLI to explain unfamiliar concepts

## 🚀 Next Steps

After completing BookBot:

1. **Explore Extensions**: Add features like word frequency analysis, reading level calculation, or a GUI interface
2. **Try Other Projects**: Use Gemini CLI to tackle more complex programming challenges
3. **Share Your Experience**: Document your learning journey and share insights
4. **Contribute**: Improve this tutorial based on your experience

## 📚 Additional Resources

- [Python Official Documentation](https://docs.python.org/)
- [Gemini CLI Documentation](https://github.com/google-gemini/gemini-cli)
- [Project Gutenberg](https://www.gutenberg.org/) - Free books for testing
- [Real Python Tutorials](https://realpython.com/) - Advanced Python learning

---

**Ready to start your AI-assisted coding journey? Follow the setup guide and dive into the tutorial!** 🚀

Happy coding with Gemini CLI! 🤖✨
