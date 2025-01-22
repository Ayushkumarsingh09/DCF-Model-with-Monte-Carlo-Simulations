import numpy as np

def monte_carlo_simulation(cash_flows, discount_rate, iterations, volatility):
    """
    Run Monte Carlo simulations to estimate NPV distributions.
    Args:
        cash_flows (list): Expected cash flows.
        discount_rate (float): Discount rate (WACC).
        iterations (int): Number of simulations.
        volatility (float): Standard deviation of cash flow changes.
    Returns:
        list: Simulated NPVs.
    """
    npvs = []
    for _ in range(iterations):
        simulated_cash_flows = [
            np.random.normal(cf, volatility * cf) for cf in cash_flows
        ]
        npvs.append(calculate_dcf(simulated_cash_flows, discount_rate))
    return npvs
