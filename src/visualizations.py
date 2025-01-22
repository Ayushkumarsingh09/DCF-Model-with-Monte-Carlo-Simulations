import matplotlib.pyplot as plt

def plot_cash_flows(cash_flows, title="Cash Flow Projections"):
    """
    Plot cash flow projections.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(cash_flows, marker='o')
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel("Cash Flow")
    plt.grid(True)
    plt.show()
