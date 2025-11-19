# --- Permutations: PIN Generator ---
import os
import sys
import itertools

# Helper to get a list of digits from user
def get_list_input(prompt):
    raw = input(prompt).strip()
    if not raw:
        print("Input cannot be empty.")
        sys.exit(1)
    return [item.strip() for item in raw.split(',') if item.strip()]

# Helper to get integer input
def get_int_input(prompt):
    try:
        val = int(input(prompt))
        if val <= 0:
            print("Please enter a positive integer.")
            sys.exit(1)
        return val
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        sys.exit(1)

# User input for digits and PIN length
print("PIN Permutation Generator")
digits = get_list_input("Enter digits to use for PIN separated by commas (e.g., 0,1,2,3,4): ")
pin_length = get_int_input("Enter the length of the PIN (e.g., 3): ")

if pin_length > len(digits):
    print("PIN length exceeds number of available digits (for permutations without replacement).")
    sys.exit(1)

# Generate permutations
permutations_without_replacement = list(itertools.permutations(digits, pin_length))
permutations_with_replacement = list(itertools.product(digits, repeat=pin_length))

# Display results
print(f"\nPIN Permutations")
print(f"Total PINs without replacement (unique digits): {len(permutations_without_replacement)}")
print(f"Total PINs with replacement (digits can repeat): {len(permutations_with_replacement)}")
