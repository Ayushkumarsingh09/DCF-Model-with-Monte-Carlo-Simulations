import unittest
from src.monte_carlo import monte_carlo_simulation

class TestMonteCarlo(unittest.TestCase):
    def test_simulation(self):
        cash_flows = [100, 200, 300]
        discount_rate = 0.1
        iterations = 1000
        volatility = 0.2

        results = monte_carlo_simulation(cash_flows, discount_rate, iterations, volatility)
        self.assertEqual(len(results), iterations)

    def test_zero_iterations(self):
        cash_flows = [100, 200, 300]
        self.assertEqual(monte_carlo_simulation(cash_flows, 0.1, 0, 0.2), [])

if __name__ == "__main__":
    unittest.main()
