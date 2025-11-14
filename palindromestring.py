import sys
# Check if argument is passed
if len(sys.argv) < 2:
    print("Error: Please pass a string as a command-line argument.")
    sys.exit(1)
string = sys.argv[1]  # Read the string from command-line
# Validate length
if len(string) < 4:
    print("String must have at least 4 characters!")
    sys.exit(1)
# Check palindrome
if string.lower() == string[::-1].lower():
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
