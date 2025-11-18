import random 

tosses=int(input())

def coin_toss():
    return random.choice(['H','T'])

def estimate_head_probability(events,n):
    return events.count('H')/n
    
def estimate_tail_probability(events,n):
    return events.count('T')/n
    



print("--- Coin Toss Results ---")

events = [coin_toss() for _ in range(tosses)]


print(estimate_head_probability(events,tosses))
print(estimate_tail_probability(events,tosses))




