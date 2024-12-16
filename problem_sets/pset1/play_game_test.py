import unittest

import warnings
def ignore_warn(*args, **kwargs):
    """Suppress all warnings."""
    pass
warnings.warn = ignore_warn

exec(open('play_game.py', 'r').read())
from play_game import estimate_win_probability

class TestEstimateWinProbability(unittest.TestCase):
    def test_probability_range(self):
        prob = estimate_win_probability(ntrials=1000)
        self.assertGreaterEqual(prob, 0.4) # 0.45 is just a placeholder.
        self.assertLessEqual(prob, 0.6) # 0.55 is just a placeholder.
            
    def test_statistical_accuracy(self):
        prob = estimate_win_probability(ntrials=100000)
        self.assertAlmostEqual(prob, 0.52, delta=0.01) # 0.52 output and the 0.01 std are just placeholders.
        
    def test_one_trial(self):
        prob = estimate_win_probability(ntrials=1)
        self.assertIn(prob, [0.0, 1.0])
        
    def test_fixed_seed(self):
        prob1 = estimate_win_probability(123, 1000)
        prob2 = estimate_win_probability(123, 1000)
        self.assertEqual(prob1, prob2)
        
if __name__ == '__main__':
    unittest.main()