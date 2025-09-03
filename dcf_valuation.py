def dcf_valuation(
    fcf,              # Expected free cash flow in year 1 (in millions)
    g,                # Perpetual growth rate (e.g., 0.03)
    r,                # Discount rate / WACC (e.g., 0.08)
    years,            # Projection years before terminal value
    growth_rate,      # Growth rate for FCF in projection years
    cash_and_equiv,   # Cash and short-term investments (in millions)
    total_debt,       # Total debt (in millions)
    shares_outstanding  # Shares outstanding (in millions)
):
    # Project FCF for `years` years using growth_rate
    fcf_projections = [fcf * (1 + growth_rate) ** i for i in range(1, years + 1)]

    # Discount FCFs to present value
    discounted_fcfs = [fcf_proj / (1 + r) ** i for i, fcf_proj in enumerate(fcf_projections, start=1)]

    # Calculate terminal value using Gordon Growth Model
    terminal_fcf = fcf_projections[-1] * (1 + g)
    terminal_value = terminal_fcf / (r - g)
    discounted_terminal = terminal_value / (1 + r) ** years

    # Sum all discounted cash flows
    enterprise_value = sum(discounted_fcfs) + discounted_terminal
    equity_value = enterprise_value + cash_and_equiv - total_debt
    price_per_share = equity_value / shares_outstanding

    return price_per_share

# Example usage
if __name__ == "__main__":
    fcf = 12000             # Free cash flow year 1 (in millions USD)
    g = 0.03                # Perpetual growth rate
    r = 0.08                # Discount rate
    years = 5               # Projection horizon
    growth_rate = 0.10      # FCF growth rate for first 5 years
    cash_and_equiv = 40000  # Cash & short-term investments
    total_debt = 28000      # Total debt
    shares_outstanding = 5200  # In millions

    dcf_price = dcf_valuation(
        fcf, g, r, years, growth_rate,
        cash_and_equiv, total_debt, shares_outstanding
    )
    print(f"Estimated intrinsic value per share: ${dcf_price:.2f}")
