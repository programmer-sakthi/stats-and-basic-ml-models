# probability code for rolling a dice in python
import random

# Function to simulate a dice roll
def roll_dice():
    return random.randint(1, 6)


# Function to calculate probabilities of each outcome after N rolls
def calculate_probabilities(n):
    outcomes = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for _ in range(n):
        roll = roll_dice()
        outcomes[roll] += 1

    probabilities = {key: value / n for key, value in outcomes.items()}

    return probabilities


# Number of trials
num_trials = 10000

# Calculate probabilities
probabilities = calculate_probabilities(num_trials)

# Print results
for face, prob in probabilities.items():
    print(f"Probability of rolling {face}: {prob:.4f}")
