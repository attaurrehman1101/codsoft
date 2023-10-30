import secrets
import string

# Function to generate a random password
def generate_password(length, complexity):
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if complexity == "low":
        chars = lower_chars + digits
    elif complexity == "medium":
        chars = lower_chars + upper_chars + digits
    elif complexity == "high":
        chars = lower_chars + upper_chars + digits + special_chars
    else:
        print("Invalid complexity level. Using medium complexity.")
        chars = lower_chars + upper_chars + digits

    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

# Get desired password length and complexity from the user
length = int(input("Enter the desired password length: "))
complexity = input("Select password complexity (low, medium, high): ").lower()

# Generate and display the password
password = generate_password(length, complexity)
print("Generated password:", password)
