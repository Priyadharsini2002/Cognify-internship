import re

def is_valid_email(email):
    # Define a regular expression pattern for a basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Use the re.match function to check if the email matches the pattern
    match = re.match(pattern, email)

    # Return True if there is a match, indicating a valid email address
    return bool(match)

# usage:
email_to_check = input("Enter an email address: ")
if is_valid_email(email_to_check):
    print(f"{email_to_check} is a valid email address.")
else:
    print(f"{email_to_check} is not a valid email address.")