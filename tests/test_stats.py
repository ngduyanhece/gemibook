"""
Test cases for BookBot stats functions
Run with: python3 -m pytest test_stats.py -v
Or: python3 test_stats.py
"""

import sys
import os

# Add parent directory to path so we can import from skeleton/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'skeleton'))

from stats import count_words, count_characters, get_character_report


def test_count_words():
    """Test word counting functionality."""
    # Test basic word counting
    text = "Hello world this is a test"
    assert count_words(text) == 6, f"Expected 6 words, got {count_words(text)}"
    
    # Test empty string
    assert count_words("") == 0, "Empty string should have 0 words"
    
    # Test single word
    assert count_words("hello") == 1, "Single word should count as 1"
    
    # Test multiple spaces
    text_spaces = "hello    world   test"
    expected = 3  # .split() handles multiple spaces
    assert count_words(text_spaces) == expected, f"Expected {expected} words with multiple spaces"
    
    # Test text with punctuation
    text_punct = "Hello, world! How are you today?"
    expected = 6  # Punctuation attached to words
    result = count_words(text_punct)
    assert result == expected, f"Expected {expected} words with punctuation, got {result}"
    
    print("✓ All word count tests passed!")


def test_count_characters():
    """Test character counting functionality."""
    # Test basic character counting
    text = "hello"
    result = count_characters(text)
    expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case insensitive
    text = "Hello"
    result = count_characters(text)
    expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert result == expected, f"Case insensitive test failed. Expected {expected}, got {result}"
    
    # Test with spaces and punctuation
    text = "hi there!"
    result = count_characters(text)
    expected = {'h': 2, 'i': 1, ' ': 1, 't': 1, 'e': 2, 'r': 1, '!': 1}
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test empty string
    result = count_characters("")
    assert result == {}, f"Empty string should return empty dict, got {result}"
    
    print("✓ All character count tests passed!")


def test_get_character_report():
    """Test character report generation."""
    # Test basic functionality
    char_count = {'a': 5, 'b': 3, 'c': 8, '!': 2, ' ': 10}
    result = get_character_report(char_count)
    
    # Should only include alphabetic characters
    expected_chars = {'a', 'b', 'c'}
    result_chars = {item['char'] for item in result}
    assert result_chars == expected_chars, f"Expected chars {expected_chars}, got {result_chars}"
    
    # Should be sorted by count (highest first)
    expected_order = [{'char': 'c', 'num': 8}, {'char': 'a', 'num': 5}, {'char': 'b', 'num': 3}]
    assert result == expected_order, f"Expected {expected_order}, got {result}"
    
    # Test with no alphabetic characters
    char_count_no_alpha = {'!': 5, ' ': 3, '1': 2}
    result = get_character_report(char_count_no_alpha)
    assert result == [], f"Expected empty list for non-alphabetic chars, got {result}"
    
    # Test empty input
    result = get_character_report({})
    assert result == [], f"Expected empty list for empty input, got {result}"
    
    print("✓ All character report tests passed!")


def run_integration_test():
    """Test the complete workflow with sample text."""
    sample_text = """
    This is a sample text for testing our BookBot implementation.
    It contains various characters, punctuation marks, and repeated letters.
    We expect 'e' and 't' to be among the most frequent characters.
    """
    
    # Test word count
    word_count = count_words(sample_text)
    print(f"Sample text word count: {word_count}")
    assert word_count > 0, "Word count should be greater than 0"
    
    # Test character count
    char_count = count_characters(sample_text)
    print(f"Sample text has {len(char_count)} unique characters")
    assert len(char_count) > 0, "Should have some characters"
    
    # Test character report
    char_report = get_character_report(char_count)
    print(f"Top 5 characters: {char_report[:5]}")
    
    # Verify report is sorted correctly
    for i in range(len(char_report) - 1):
        current_count = char_report[i]['num']
        next_count = char_report[i + 1]['num']
        assert current_count >= next_count, "Character report should be sorted by count (descending)"
    
    print("✓ Integration test passed!")


def main():
    """Run all tests."""
    print("Running BookBot Tests...")
    print("=" * 40)
    
    try:
        test_count_words()
        test_count_characters() 
        test_get_character_report()
        run_integration_test()
        
        print("=" * 40)
        print("🎉 ALL TESTS PASSED! Your BookBot implementation is working correctly.")
        
    except AssertionError as e:
        print(f"❌ TEST FAILED: {e}")
        print("Check your implementation and try again.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ ERROR: {e}")
        print("Make sure all functions are implemented correctly.")
        sys.exit(1)


if __name__ == "__main__":
    main()