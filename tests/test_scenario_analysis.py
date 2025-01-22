import unittest
from src.scenario_analysis import scenario_analysis

class TestScenarioAnalysis(unittest.TestCase):
    def test_analysis(self):
        scenarios = {
            "pessimistic": [80, 150, 200],
            "base_case": [100, 200, 300],
            "optimistic": [120, 250, 400]
        }
        discount_rate = 0.1

        results = scenario_analysis(scenarios, discount_rate)
        self.assertEqual(set(results.keys()), {"pessimistic", "base_case", "optimistic"})

if __name__ == "__main__":
    unittest.main()
