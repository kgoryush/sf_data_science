"""Game: Guess the number. 
The comp sets and guesses the number by himself."""

import numpy as np

def random_predict(number:int=1) -> int:
    """Guess the number randomly
    Args: 
        number (int, optional): The number is set. Defaults to 1.
    Returns:
        int: Number of attempts"""

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1,101) # proposed number
        if number == predict_number:
            break # exit from the cycle if the number is guessed
    return(count)

print(f"Number of attempts: {random_predict()}")

def score_game(random_predict) -> int:
    """In how many attemps in average from 1000 times our algorithm guesses the number
    Args:
        random_predict ([type]): guess function
    Returns:
        int: average number of attempts"""

    count_ls = [] # list for attempts
    np.random.seed(1) # fix seed for repeatability
    random_array = np.random.randint(1,101, size=(1000)) # set list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) # find average number of attempts

    print(f"Your algorithm guesses the number in average in: {score} attempts")
    return(score)

# RUN
if __name__=='__main__':
    score_game(random_predict)