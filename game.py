"""Guess the number"""

import numpy as np

number = np.random.randint(1,101) # set the number randomly from 1 to 100
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100"))
    
    if predict_number > number:
        print("The number should be less!")
    elif predict_number < number:
        print("The number should be larger!")
        
    else:
        print(f"You have guessed the number! The number = {number}, in {count} attempts")
        break # game end, exit from the cycle
    