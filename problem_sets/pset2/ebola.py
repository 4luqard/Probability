import numpy as np
import polars as pl

def calculate_probs(filename):
    data = pl.read_csv(filename)
    probas = [0] * 6
    for i in range(6):
        if i != 5:
            probas[i] = len(data.filter(pl.col(f'G_{i+1}') == 1)) / len(data)
        else:
            probas[i] = len(data.filter(pl.col('T') == 1)) / len(data)
    return probas


def calculate_cond_probs(filename):
    data = pl.read_csv(filename)
    cond_probas = [0] * 5
    for i in range(5):
        cond_probas[i] = len(data.filter(pl.col(f'G_{i+1}') == 1).filter(pl.col('T') == 1)) / len(data.filter(pl.col(f'G_{i+1}') == 1))
    return cond_probas

def main():
    """
    This script contains a main function that demonstrates probability calculations using data from
    'bats.csv'. The function calls two separate functions, calculate_probs and calculate_cond_probs, 
    to compute basic probabilities and conditional probabilities respectively, and prints the results 
    to the console for verification or further analysis.

    File:
        ebola.py

    Functions:
        main():
            Reads data from 'bats.csv'.
            Calls calculate_probs(filename) to compute initial probabilities.
            Calls calculate_cond_probs(filename) to compute conditional probabilities.
            Prints the computed probabilities for inspection.
    """
    filename = 'bats.csv'

    print("****** Calling calculate_probs on 'bats.csv' *******")
    probs = calculate_probs(filename)
    print(f"\treturned {probs}")
    print("*********************************************\n")

    print("*** Beginning calculate_cond_probs on 'bats.csv' ***")
    cond_probs = calculate_cond_probs(filename)
    print(f"\treturned {cond_probs}")
    print("*********************************************\n")

################################################################################
if __name__ == "__main__":
    main()