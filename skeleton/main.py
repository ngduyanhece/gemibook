"""
BookBot - Text Analysis Tool
Main entry point for the program
"""

import sys
from stats import count_words, count_characters, get_character_report


def get_book_text(path):
    """
    Read and return the contents of a text file.
    
    Args:
        path (str): Path to the text file
        
    Returns:
        str: Contents of the file
    """
    # TODO: Implement file reading using 'with' statement and .read() method
    pass


def main():
    """
    Main function that orchestrates the book analysis.
    """
    # TODO: Check command line arguments using sys.argv
    # Should have exactly 2 arguments (script name + book path)
    # If not, print usage message and exit with sys.exit(1)
    
    # TODO: Get the book path from command line arguments
    book_path = None  # Replace with actual path from sys.argv
    
    # TODO: Read the book text using get_book_text()
    text = None
    
    # TODO: Count words using count_words() from stats.py
    word_count = None
    
    # TODO: Count characters using count_characters() from stats.py  
    char_count = None
    
    # TODO: Get sorted character report using get_character_report() from stats.py
    char_report = None
    
    # TODO: Print the formatted report
    # Format:
    # ============ BOOKBOT ============
    # Analyzing book found at {book_path}...
    # ----------- Word Count ----------
    # Found {word_count} total words
    # --------- Character Count -------
    # {char}: {count}
    # {char}: {count}
    # ...
    # ============= END ===============
    
    pass


if __name__ == "__main__":
    main()