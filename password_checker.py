import re

def check_password_strength(password):
    # Criteria
    length_error = len(password) < 8
    lowercase_error = not re.search(r"[a-z]", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    digit_error = not re.search(r"\d", password)
    special_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Count how many rules passed
    passed_criteria = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_error])

    # Assign strength level
    if passed_criteria <= 2:
        strength = "Weak"
    elif passed_criteria == 3:
        strength = "Medium"
    elif passed_criteria == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    # Detailed feedback
    feedback = []
    if length_error: feedback.append("Password should be at least 8 characters long.")
    if lowercase_error: feedback.append("Include at least one lowercase letter.")
    if uppercase_error: feedback.append("Include at least one uppercase letter.")
    if digit_error: feedback.append("Include at least one number.")
    if special_error: feedback.append("Include at least one special character (!@#$ etc).")

    return strength, feedback


if __name__ == "__main__":   # <- This line is correct Python syntax
    password = input("Enter a password: ")
    strength, feedback = check_password_strength(password)

    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(" -", f)