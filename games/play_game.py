import numpy as np

def estimate_win_probability(ntrials: int = 100000) -> float:
    """
    Simulate a game where two players add random integers between 1 and 100 to a running total.

    The game starts with a sum S = 0.
    - Player one adds random numbers until S > 100, recording their last number x.
    - Player two continues adding numbers until S > 200, recording their last number y.
    The player with the higher last number wins (if y > x, player two wins).

    ntrials: the number of trials to run.

    return: the estimated probability that the second player wins.
    """
    player_two_win = 0
    for i in range(ntrials):
        
        S = 0
        
        while S < 100:
            player_one_last_value = np.random.randint(1, 101)
            S += player_one_last_value
        
        while S < 200:
            player_two_last_value = np.random.randint(1, 101)
            S += player_two_last_value
        
        player_two_win += player_two_last_value > player_one_last_value
    
    return player_two_win / ntrials

print(estimate_win_probability())