#check whether the given string is palindrome or not
string = input("Enter a string (minimum 4 characters): ")

if len(string) < 4:
    print("String must have at least 4 characters!")
else:
    # Check palindrome (case-insensitive)
    if string.lower() == string[::-1].lower():
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
