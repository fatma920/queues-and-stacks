def is_palindrome(input_string):
    # Remove non-alphanumeric characters and convert to lowercase
    clean_string = ''.join(char for char in input_string if char.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return clean_string == clean_string[::-1]

# Test cases
input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")
