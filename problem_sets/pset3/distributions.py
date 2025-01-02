from numpy.random import rand


# part (a) - completed for you
def simulate_bernoulli(p: float = 0.4):
    if rand() < p:
        return 1
    return 0


# part (b)
def simulate_binomial(n: int = 20, p: float = 0.4):
    pass  # TODO: delete this line and implement this function!


# part (c)
def simulate_geometric(p: float = 0.03):
    pass  # TODO: delete this line and implement this function!


# part (d)
def simulate_neg_binomial(r: int = 5, p: float = 0.03):
    pass  # TODO: delete this line and implement this function!


# part (e)
def simulate_poisson(poi_lambda: float = 3.1):
    pass  # TODO: delete this line and implement this function!


# part (f)
def simulate_exponential(exp_lambda: float = 3.1):
    pass  # TODO: delete this line and implement this function!
