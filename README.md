This project implements a comprehensive Discounted Cash Flow (DCF) valuation model to estimate the intrinsic value of a company.
The model projects revenues and free cash flows, applies discounting using the Weighted Average Cost of Capital (WACC), and calculates terminal value using both the perpetuity growth and exit multiple methods.
It also features sensitivity analysis to test different assumptions and provides visual outputs for better interpretation of results.
The repository includes an example script (example_tsm_dcf.py) showing how to fetch financial data from Yahoo Finance and run the DCF model automatically.
🔎 What the script does
Selects ticker
2330.TW → TSMC ordinary shares in TWD
TSM → TSMC ADR traded in USD (⚠️ 1 ADR = 5 ordinary shares)
Fetches financials
From the cash flow statement: Operating Cash Flow and Capital Expenditure
Calculates Free Cash Flow = OCF − CapEx
Retrieves cash, total debt, and shares outstanding
Applies assumptions
Sets projection growth rate, WACC (discount rate), and terminal growth
Calls your dcf_valuation() function with these inputs
Outputs valuation
Enterprise Value (EV)
Equity Value per Share
