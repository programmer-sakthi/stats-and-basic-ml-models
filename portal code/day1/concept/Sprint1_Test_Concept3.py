import os
import sys
import pandas as pd

# Function to safely get integer input
def get_int_input(prompt):
    try:
        value = int(input(prompt))
        if value < 0:
            print("Please enter a non-negative integer.")
            sys.exit(1)
        return value
    except ValueError:
        print("Invalid input! Please enter an integer.")
        sys.exit(1)

# Get user input for Latte and Black Coffee counts for each age group
#print("Enter the number of customers for each coffee preference by age group:")

age_groups = ['18–25', '26–40', '40+']
coffee_types = ['Latte', 'Black Coffee']

data = {coffee: [] for coffee in coffee_types}

for age in age_groups:
    print(f"\nAge group: {age}")
    for coffee in coffee_types:
        count = get_int_input(f"Number of customers who prefer {coffee}: ")
        data[coffee].append(count)

# Create DataFrame
df = pd.DataFrame(data, index=age_groups)

total_customers = df.values.sum()
if total_customers == 0:
    print("No data provided (total customers = 0). Exiting.")
    sys.exit(1)

print("\nData Summary:")
print(df)

# What is the probability of older customers prefer Black Coffee?
joint_prob_older_black = df.loc['40+', 'Black Coffee'] / total_customers
print(f"\nJoint Probability P(Age 40+ and Black Coffee): {joint_prob_older_black:.4f}")

# What’s the Probability of customers prefer Black Coffee if Age > 40?
total_40plus = df.loc['40+'].sum()
if total_40plus == 0:
    print("No customers in the 40+ age group, conditional probability undefined.")
    sys.exit(1)

black_40plus = df.loc['40+', 'Black Coffee']
cond_prob_black_given_40plus = black_40plus / total_40plus
print(f"Conditional Probability P(Black Coffee | Age 40+): {cond_prob_black_given_40plus:.4f}")

# Does age influence black coffee preference?
overall_prob_black = df['Black Coffee'].sum() / total_customers
print(f"\nOverall Probability P(Black Coffee): {overall_prob_black:.4f}")
print(f"Conditional Probability P(Black Coffee | Age 40+): {cond_prob_black_given_40plus:.4f}")

if abs(cond_prob_black_given_40plus - overall_prob_black) < 1e-4:
    print("Age (being 40 or older) does NOT influence preference for Black Coffee.")
else:
    print("Age (being 40 or older) influences preference for Black Coffee.")


# Program Description: 

# Create the Python program calculates the total number of possible PIN codes that can be generated using a set of user-defined digits, with two conditions:

# Without Replacement: Digits in the PIN do not repeat

# With Replacement: Digits can repeat in the PIN

# It utilizes Python's itertools module and takes all input directly from the user.

# Input format :
# The program accepts two user inputs:

# Digits: A list of characters or numbers, separated by commas

# Example: 0,1,2,3,4

# PIN Length: An integer specifying how many digits the PIN should contain

# Example: 3

# Output format :
# After receiving inputs, the program displays:

# The total number of unique-digit PINs (no digit is repeated – permutation without replacement)

# The total number of PINs with repeated digits allowed (permutation with replacement)

# Code constraints :
# The list of digits must not be empty

# The PIN length must be a positive integer

# The PIN length must not exceed the number of digits when calculating permutations without replacement

# If any input is invalid, the program will show an error and exit

# Sample test cases :
# Input 1 :
# 0,1,2,3,4
# 3
# Output 1 :
# PIN Permutation Generator
# Enter digits to use for PIN separated by commas (e.g., 0,1,2,3,4): Enter the length of the PIN (e.g., 3): 
# PIN Permutations
# Total PINs without replacement (unique digits): 60
# Total PINs with replacement (digits can repeat): 125