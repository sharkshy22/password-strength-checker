# ------------------------------------------------------------
# Project: Password Strength Checker
# Author: Dev Gupta
# Description: Checks if a password is Strong, Moderate, or Weak
# ------------------------------------------------------------

import re
import string
import getpass  # optional, to hide password input

def check_password_strength(password):
    """
    Function to evaluate password strength based on:
    - Length
    - Uppercase letters
    - Lowercase letters
    - Numbers
    - Special symbols
    """
    # Conditions
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(f"[{re.escape(string.punctuation)}]", password) is None

    # Count how many conditions are met
    conditions_met = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    # Evaluate strength
    if conditions_met == 5:
        strength = "Strong 💪"
    elif 3 <= conditions_met < 5:
        strength = "Moderate 😐"
    else:
        strength = "Weak ⚠️"

    # Print detailed result
    print("\nPassword Strength Report:")
    print(f"✔ Length (8+ characters): {'OK' if not length_error else 'Missing'}")
    print(f"✔ Contains number: {'OK' if not digit_error else 'Missing'}")
    print(f"✔ Contains uppercase letter: {'OK' if not uppercase_error else 'Missing'}")
    print(f"✔ Contains lowercase letter: {'OK' if not lowercase_error else 'Missing'}")
    print(f"✔ Contains symbol: {'OK' if not symbol_error else 'Missing'}")
    print(f"\nOverall Strength → {strength}")
    return strength


def main():
    print("========================================")
    print("     🔐 PASSWORD STRENGTH CHECKER")
    print("========================================\n")

    # Input password (hidden)
    password = input("Enter your password: ")
    print(password)

    # Evaluate password
    check_password_strength(password)

    print("\nThank you for using the Password Strength Checker!")
    print("========================================")
# Run program
if __name__ == "__main__":
    main()
