import numpy as np

def calculate_dcf(cash_flows, discount_rate):
    """
    Calculate the net present value (NPV) of cash flows.
    Args:
        cash_flows (list): List of future cash flows.
        discount_rate (float): Discount rate (WACC).
    Returns:
        float: Net Present Value (NPV).
    """
    npv = sum(cf / (1 + discount_rate) ** t for t, cf in enumerate(cash_flows, start=1))
    return npv
