import unittest
from play_game import estimate_win_probability

import warnings
def ignore_warn(*args, **kwargs):
    """Suppress all warnings."""
    pass
warnings.warn = ignore_warn

class TestEstimateWinProbability(unittest.TestCase):
    def test_statistical_accuracy(self):
        prob = estimate_win_probability(ntrials=1000000)
        self.assertAlmostEqual(prob, 0.5215, delta=0.0015)
        
    def test_one_trial(self):
        prob = estimate_win_probability(ntrials=1)
        self.assertIn(prob, [0.0, 1.0])
        
    def test_fixed_seed(self):
        prob1 = estimate_win_probability(123, 1000)
        prob2 = estimate_win_probability(123, 1000)
        self.assertEqual(prob1, prob2)
        
if __name__ == '__main__':
    unittest.main()