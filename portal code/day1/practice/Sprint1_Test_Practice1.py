print("BuyBloom Probability Calculator")
n=int(input("Enter total number of orders shipped: "))
r=int(input("Enter number of orders returned: "))

p= (n-r)/n
print(f"Probability a randomly selected order was NOT returned: {p:.4f}")
print()

partners=int(input("Enter total number of delivery partners: "))
delayed=int(input("Enter number of delayed partners: "))
on_time = partners - delayed

# probability that first partner arrives on time 
p1=on_time/partners

# probability that second partner arrives on time given first arrives on time 
# 1 partner who is on time will be removed - on_time-1 , partners - 1 
p2=(on_time-1)/(partners-1)

p=p1*p2

print(f"Probability both randomly chosen partners are on time: {p:.4f}")

print()

discount_prob=float(input("Enter probability of a product getting a discount (0 to 1): "))
n=int(input("Enter number of products chosen: "))

p=pow(discount_prob,n)

print(f"Probability all {n} randomly chosen products get discount: {p:.4f}")

print()
n=int(input("Enter total number of days in the period (e.g., 7): "))
days=int(input("Enter number of days with deals (out of 7): "))

p=days/n
print(f"Probability of finding a deal on a random day: {p:.4f}")



# Program Description:

# Create the program helps BuyBloom analyze customer behavior and logistics using basic probability calculations.

# The program handles four business scenarios:

# Order Return Probability:

# Given the total number of orders shipped and the number of returned orders, it calculates the probability that a randomly selected order was not returned.

# Delivery Partner On-Time Probability:

# Based on the total number of delivery partners and the count of those delayed, it calculates the probability that two randomly chosen partners are both on time (selected without replacement).

# Flash Sale Discount Probability:

# Given the probability of a single product receiving a discount during a flash sale, and the number of products chosen, it calculates the probability that all selected products get a discount.

# Flash Deal Day Probability:

# Considering the number of days in a week and the specific days when flash deals run, it calculates the probability that logging in on a random day finds an active flash deal.

# Input format :
# Total number of orders shipped (integer)

# Number of returned orders (integer)

# Total delivery partners (integer)

# Number of delayed partners (integer)

# Probability of discount on a single product (decimal between 0 and 1)

# Number of products chosen for discount check (integer)

# Total days in a week (integer)

# Number of flash deal days in the week (integer)

# Output format :
# Probability that a randomly selected order was not returned (rounded to 2 decimal places)

# Probability that two randomly chosen delivery partners are both on time (rounded to 4 decimal places)

# Probability that all chosen products get a discount (rounded to 3 decimal places)

# Probability of finding a flash deal when logging in on a random day (rounded to 4 decimal places)

# Code constraints :
# All input values should be valid positive numbers, with probabilities between 0 and 1.

# Number of delayed partners must not exceed total delivery partners.

# Number of products chosen must be a positive integer.

# Number of flash deal days must not exceed total days in a week.

# Sample test cases :
# Input 1 :
# 100
# 8
# 50
# 5
# 0.7
# 3
# 7
# 3
# Output 1 :
# BuyBloom Probability Calculator
# Enter total number of orders shipped: Enter number of orders returned: Probability a randomly selected order was NOT returned: 0.9200

# Enter total number of delivery partners: Enter number of delayed partners: Probability both randomly chosen partners are on time: 0.8082

# Enter probability of a product getting a discount (0 to 1): Enter number of products chosen: Probability all 3 randomly chosen products get discount: 0.3430

# Enter total number of days in the period (e.g., 7): Enter number of days with deals (out of 7): Probability of finding a deal on a random day: 0.4286