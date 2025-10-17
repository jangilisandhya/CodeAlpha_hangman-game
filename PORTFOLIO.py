# Stock Portfolio Tracker

# Hardcoded stock prices (in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 350
}

# Ask user for stock inputs
portfolio = {}
n = int(input("Enter the number of stocks you own: "))

for i in range(n):
    stock = input(f"Enter stock {i+1} symbol (e.g., AAPL): ").upper()
    quantity = int(input(f"Enter quantity of {stock}: "))
    if stock in stock_prices:
        portfolio[stock] = quantity
    else:
        print(f"{stock} not in database. Skipping...")

# Calculate total investment
total_investment = 0
for stock, qty in portfolio.items():
    total_investment += qty * stock_prices[stock]

# Display result
print("\n----- Portfolio Summary -----")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${qty * stock_prices[stock]}")
print(f"\nTotal Investment Value: ${total_investment}")

# Save result to file (optional)
with open("portfolio_summary.txt", "w") as file:
    file.write("----- Portfolio Summary -----\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
    file.write(f"\nTotal Investment Value: ${total_investment}\n")

print("\nPortfolio summary saved to 'portfolio_summary.txt'")
