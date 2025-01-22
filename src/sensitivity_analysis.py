def sensitivity_analysis(base_cash_flows, discount_rate, factors):
    """
    Perform sensitivity analysis for changes in cash flows or discount rates.
    Args:
        base_cash_flows (list): Base case cash flows.
        discount_rate (float): Discount rate.
        factors (list): Percentage change factors (e.g., [-0.1, 0, 0.1]).
    Returns:
        dict: Mapping of factor to NPV.
    """
    results = {}
    for factor in factors:
        adjusted_cash_flows = [cf * (1 + factor) for cf in base_cash_flows]
        results[factor] = calculate_dcf(adjusted_cash_flows, discount_rate)
    return results
