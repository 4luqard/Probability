from numpy.random import rand


# part (a) - completed for you
def simulate_bernoulli(p: float = 0.4):
    if rand() < p:
        return 1
    return 0


# part (b)
def simulate_binomial(n: int = 20, p: float = 0.4):
    successes = 0
    for i in range(n):
        successes += simulate_bernoulli(p)
    return successes


# part (c)
def simulate_geometric(p: float = 0.03):
    count = 0
    while simulate_bernoulli(p) == 0:
        count += 1
    return count + 1


# part (d)
def simulate_neg_binomial(r: int = 5, p: float = 0.03):
    count = 0
    for i in range(r):
        count += simulate_geometric(p)
    return count


# part (e)
# Approximation of Poisson distribution
def simulate_poisson(poi_lambda: float = 3.1):
    return simulate_binomial(60000, poi_lambda / 60000)


# part (f)
def simulate_exponential(exp_lambda: float = 3.1):
    return simulate_geometric(exp_lambda / 60000) / 60000
