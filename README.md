import yfinance as yf
from dcf_valuation import dcf_valuation

ticker = yf.Ticker("2330.TW")  # or "TSM" for ADR

# Free Cash Flow from OCF and CapEx
ocf = float(ticker.cashflow.loc["Operating Cash Flow"].dropna().iloc[0])
capex = abs(float(ticker.cashflow.loc["Capital Expenditure"].dropna().iloc[0]))
fcf_twd = ocf - capex

# Balance sheet items
cash = float(ticker.balance_sheet.loc["Cash And Cash Equivalents"].dropna().iloc[0])
debt = float(ticker.balance_sheet.loc["Total Debt"].dropna().iloc[0])
shares = ticker.shares_outstanding

# Assumptions
growth_rate, years, wacc, g_term = 0.05, 5, 0.08, 0.03

# Run DCF
vps, ev = dcf_valuation(
    fcf=fcf_twd/1e6,
    growth_rate=growth_rate,
    years=years,
    r=wacc,
    g=g_term,
    cash_and_equiv=cash/1e6,
    total_debt=debt/1e6,
    shares_outstanding=shares/1e6
)

print(f"EV (TWD, millions): {ev:,.2f}")
print(f"Equity Value per Share (TWD): {vps:,.2f}")
