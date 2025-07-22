"""
BookBot - Text Analysis Functions
Contains functions for analyzing text statistics
"""


def count_words(text):
    """
    Count the number of words in the given text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        int: Number of words in the text
    """
    # TODO: Split the text into words and return the count
    # Hint: Use the .split() method and len() function
    pass


def count_characters(text):
    """
    Count the frequency of each character in the text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: Dictionary mapping characters to their counts
              Example: {'a': 1234, 'b': 567, ' ': 8901, ...}
    """
    # TODO: Create an empty dictionary to store character counts
    char_count = {}
    
    # TODO: Iterate through each character in the text
    # Convert to lowercase using .lower() method
    # Count each character in the dictionary
    # Hint: Check if character exists in dict, if not initialize to 0
    
    return char_count


def get_character_report(char_count):
    """
    Convert character count dictionary to a sorted list for reporting.
    
    Args:
        char_count (dict): Dictionary of character counts
        
    Returns:
        list: List of dictionaries sorted by count (highest first)
              Only includes alphabetic characters
              Example: [{"char": "e", "num": 44538}, {"char": "t", "num": 29493}, ...]
    """
    # TODO: Create empty list to store character report data
    char_list = []
    
    # TODO: Iterate through the character count dictionary
    # For each character, check if it's alphabetic using .isalpha() method
    # If alphabetic, create a dictionary with "char" and "num" keys
    # Add the dictionary to the char_list
    
    # TODO: Sort the list by count (highest first)
    # Hint: Use .sort() method with reverse=True and key parameter
    # You'll need a function that returns the "num" value for sorting
    
    return char_list


def sort_on(dict_item):
    """
    Helper function for sorting - returns the 'num' value from dictionary.
    
    Args:
        dict_item (dict): Dictionary with 'num' key
        
    Returns:
        int: The value of the 'num' key
    """
    # TODO: Return the "num" value from the dictionary
    # This function is used as the key parameter in .sort()
    pass