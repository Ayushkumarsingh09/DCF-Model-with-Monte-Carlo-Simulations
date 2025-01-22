def scenario_analysis(scenarios, discount_rate):
    """
    Perform scenario analysis based on predefined cash flow scenarios.
    Args:
        scenarios (dict): Mapping of scenario names to cash flows.
        discount_rate (float): Discount rate.
    Returns:
        dict: Scenario results with NPVs.
    """
    results = {}
    for scenario, cash_flows in scenarios.items():
        results[scenario] = calculate_dcf(cash_flows, discount_rate)
    return results
