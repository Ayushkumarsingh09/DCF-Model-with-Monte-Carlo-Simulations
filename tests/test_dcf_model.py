import unittest
from src.dcf_model import calculate_dcf

class TestDCFModel(unittest.TestCase):
    def test_calculate_dcf(self):
        cash_flows = [100, 200, 300]
        discount_rate = 0.1
        expected_npv = sum(cf / (1 + discount_rate) ** t for t, cf in enumerate(cash_flows, start=1))
        self.assertAlmostEqual(calculate_dcf(cash_flows, discount_rate), expected_npv)

    def test_empty_cash_flows(self):
        self.assertEqual(calculate_dcf([], 0.1), 0)

if __name__ == "__main__":
    unittest.main()
