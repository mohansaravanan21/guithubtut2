def is_palindrome_recursive(s: str) -> bool:
    """
    Check if a string is a palindrome using recursion.

    :param s: Input string
    :return: True if the string is a palindrome, False otherwise
    """
    # Base case: if the string has 0 or 1 character, it's a palindrome
    if len(s) <= 1:
        return True

    # Check the first and last characters
    if s[0] != s[-1]:
        return False

    # Recursive case: check the substring excluding the first and last characters
    return is_palindrome_recursive(s[1:-1])

# Example usage
if __name__ == "__main__":
    test_string = "radar"
    print(f"Is '{test_string}' a palindrome? {is_palindrome_recursive(test_string)}")