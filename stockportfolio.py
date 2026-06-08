# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker
def stock_tracker():

    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 150,
        "MSFT": 320
    }

    portfolio = {}
    total_value = 0

    print("=== Stock Portfolio Tracker ===")

    while True:

        print("\nMenu")
        print("1. View Available Stocks")
        print("2. Add New Stock")
        print("3. Buy Stocks")
        print("4. Exit and Show Portfolio")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nAvailable Stocks:")
            for stock, price in stock_prices.items():
                print(f"{stock} : ${price}")

        elif choice == "2":
            new_stock = input("Enter new stock name: ").upper()

            if new_stock in stock_prices:
                print("Stock already exists!")
            else:
                new_price = float(input("Enter stock price: "))
                stock_prices[new_stock] = new_price
                print(f"{new_stock} added successfully!")

        elif choice == "3":
            stock_name = input("Enter stock name: ").upper()

            if stock_name in stock_prices:
                quantity = int(input("Enter quantity: "))
                portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
                print("Stock added to portfolio!")
            else:
                print("Stock not available!")

        elif choice == "4":
            break

        else:
            print("Invalid choice! Please try again.")

    print("\n===== PORTFOLIO SUMMARY =====")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        total_value += value

        print(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${stock_prices[stock]} | "
            f"Value: ${value}"
        )

    print(f"\nTotal Portfolio Value: ${total_value}")


stock_tracker()
