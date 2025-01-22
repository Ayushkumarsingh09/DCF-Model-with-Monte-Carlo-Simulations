import unittest
from src.sensitivity_analysis import sensitivity_analysis

class TestSensitivityAnalysis(unittest.TestCase):
    def test_analysis(self):
        cash_flows = [100, 200, 300]
        discount_rate = 0.1
        factors = [-0.1, 0, 0.1]

        results = sensitivity_analysis(cash_flows, discount_rate, factors)
        self.assertEqual(len(results), len(factors))

if __name__ == "__main__":
    unittest.main()
