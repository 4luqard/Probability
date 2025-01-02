import pytest
import numpy as np
import scipy.stats as stats

from distributions import (
    simulate_bernoulli,
    simulate_binomial,
    simulate_geometric,
    simulate_neg_binomial,
    simulate_poisson,
    simulate_exponential,
)


def test_simulate_bernoulli():
    p = 0.13
    n = 10000
    simulated = [simulate_bernoulli(p) for _ in range(n)]
    assert np.isclose(np.mean(simulated), p, atol=p * (1 - p))


def test_simulate_binomial():
    n = 20
    p = 0.82
    simulated = [simulate_binomial(n, p) for _ in range(10000)]
    assert np.isclose(np.mean(simulated), n * p, atol=n * p * (1 - p))


def test_simulate_geometric():
    p = 0.46
    n = 10000
    simulated = [simulate_geometric(p) for _ in range(n)]
    assert np.isclose(np.mean(simulated), 1 / p, atol=(1 - p) / p**2)


def test_simulate_neg_binomial():
    r = 5
    p = 0.33
    n = 10000
    simulated = [simulate_neg_binomial(r, p) for _ in range(n)]
    assert np.isclose(np.mean(simulated), r / p, atol=(r * (1 - p)) / p**2)


def test_simulate_poisson():
    poi_lambda = 4.2
    n = 100
    simulated = [simulate_poisson(poi_lambda) for _ in range(n)]
    assert np.isclose(np.mean(simulated), poi_lambda, atol=poi_lambda)


def test_simulate_exponential():
    exp_lambda = 3.1
    n = 100
    simulated = [simulate_exponential(exp_lambda) for _ in range(n)]
    assert np.isclose(np.mean(simulated), 1 / exp_lambda, atol=1 / exp_lambda**2)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
