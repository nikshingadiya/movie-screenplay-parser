import re

def remove_page_number(text, pattern=r'^\d+\.*$'):
    regex_pattern = re.compile(pattern)  # Regular expression pattern
    if regex_pattern.match(text):
        return True
    return False

# Example usage
pattern_to_check = r'^\d+\.*$'  # Pattern to check for any number followed by zero or more dots

x="4."
print(remove_page_number(text=x, pattern=pattern_to_check))  # Output: True
