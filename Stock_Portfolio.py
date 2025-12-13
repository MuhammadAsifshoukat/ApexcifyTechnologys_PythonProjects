# STOCK_PORTFOLIO

def show_stocks(prices):
    print("\nAvailable Stocks:")
    for stock, price in prices.items():
        print(f"{stock} : ${price}")


def calculate_portfolio(prices):
    total = 0
    portfolio = {}

    while True:
        stock = input("\nEnter stock name (or 'done' to finish): ").upper()
        if stock == "DONE":
            break

        if stock in prices:
            qty = int(input("Enter quantity: "))
            value = prices[stock] * qty
            portfolio[stock] = value
            total += value
        else:
            print(" Stock not found!")

    return portfolio, total


stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

show_stocks(stock_prices)

portfolio, total_value = calculate_portfolio(stock_prices)

print("\n📊 Portfolio Summary")
for stock, value in portfolio.items():
    print(f"{stock} Investment: ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

with open("portfolio.txt", "w") as file:
    file.write("Portfolio Summary\n")
    for stock, value in portfolio.items():
        file.write(f"{stock}: ${value}\n")
    file.write(f"\nTotal Investment: ${total_value}")

print("\n✅ Data saved to portfolio.txt")
