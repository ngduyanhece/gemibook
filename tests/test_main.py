"""
Test cases for BookBot main functionality
Tests command-line argument handling and file operations
"""

import sys
import os
import subprocess
import tempfile
from unittest.mock import patch

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'skeleton'))


def test_command_line_args():
    """Test command-line argument validation."""
    skeleton_dir = os.path.join(os.path.dirname(__file__), '..', 'skeleton')
    main_py = os.path.join(skeleton_dir, 'main.py')
    
    # Test no arguments (should show usage)
    result = subprocess.run([sys.executable, main_py], 
                          capture_output=True, text=True)
    assert result.returncode == 1, "Should exit with code 1 when no arguments provided"
    assert "Usage:" in result.stdout or "usage:" in result.stdout.lower(), "Should show usage message"
    
    print("✓ Command-line argument validation test passed!")


def test_file_reading():
    """Test file reading functionality."""
    # Create a temporary test file
    test_content = "Hello world!\nThis is a test file.\nIt has multiple lines."
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(test_content)
        temp_file = f.name
    
    try:
        # Import and test get_book_text function
        from main import get_book_text
        
        result = get_book_text(temp_file)
        assert result == test_content, f"Expected '{test_content}', got '{result}'"
        
        print("✓ File reading test passed!")
        
    except ImportError:
        print("⚠️  get_book_text function not implemented yet")
    except Exception as e:
        print(f"❌ File reading test failed: {e}")
    finally:
        # Clean up temp file
        os.unlink(temp_file)


def test_full_program():
    """Test the complete program with a sample file."""
    # Create sample book file
    sample_book = """
    The quick brown fox jumps over the lazy dog.
    This sentence contains every letter of the alphabet.
    Perfect for testing character counting functionality.
    """
    
    skeleton_dir = os.path.join(os.path.dirname(__file__), '..', 'skeleton')
    main_py = os.path.join(skeleton_dir, 'main.py')
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(sample_book)
        temp_file = f.name
    
    try:
        # Run the program
        result = subprocess.run([sys.executable, main_py, temp_file], 
                              capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            output = result.stdout
            # Check for expected output format
            if "BOOKBOT" in output and "words found" in output.lower():
                print("✓ Full program test passed!")
                print("Output preview:")
                print(output[:200] + "..." if len(output) > 200 else output)
            else:
                print("⚠️  Program runs but output format may need adjustment")
                print("Actual output:", output[:200])
        else:
            print("⚠️  Program not fully implemented yet")
            if result.stderr:
                print("Error:", result.stderr)
                
    except subprocess.TimeoutExpired:
        print("⚠️  Program timed out - may have an infinite loop")
    except Exception as e:
        print(f"❌ Full program test error: {e}")
    finally:
        os.unlink(temp_file)


def main():
    """Run main functionality tests."""
    print("Running BookBot Main Tests...")
    print("=" * 40)
    
    test_command_line_args()
    test_file_reading() 
    test_full_program()
    
    print("=" * 40)
    print("Main functionality tests completed!")


if __name__ == "__main__":
    main()