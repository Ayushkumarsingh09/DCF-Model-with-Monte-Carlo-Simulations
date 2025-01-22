def adjust_discount_rate(base_rate, risk_premium):
    """
    Adjust the discount rate based on risk premium.
    Args:
        base_rate (float): Base discount rate.
        risk_premium (float): Additional risk premium.
    Returns:
        float: Adjusted discount rate.
    """
    return base_rate + risk_premium
