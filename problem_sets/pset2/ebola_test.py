import unittest
import numpy as np
from ebola import calculate_probs, calculate_cond_probs

import warnings
def ignore_warn(*args, **kwargs):
    """Suppress all warnings."""
    pass
warnings.warn = ignore_warn

class TestEstimateWinProbability(unittest.TestCase):
    def setUp(self):
        self.filename = 'problem_sets/pset2/bats.csv'
        self.probas = [0.70228, 0.30076, 0.5009, 0.80162, 0.32705, 0.30079]
        self.cond_probas = [0.30201628979894063, 0.30220109057055455, 
                            0.5831902575364344, 0.37053716224645095, 0.8999847118177648]
        
    def test_calculate_probs(self):
        probas = calculate_probs(self.filename)
        for i in range(6):
            self.assertAlmostEqual(probas[i], self.probas[i], places=5)
        
    def test_calculate_cond_probs(self):
        cond_probas = calculate_cond_probs(self.filename)
        for i in range(5):
            self.assertAlmostEqual(cond_probas[i], self.cond_probas[i], places=5) 

if __name__ == '__main__':
    unittest.main()