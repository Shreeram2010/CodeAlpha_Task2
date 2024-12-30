import requests

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
        
    def add_stock(self, ticker, shares):
        if ticker in self.portfolio:
            self.portfolio[ticker]['shares'] += shares
        else:
            self.portfolio[ticker] = {'shares': shares, 'price': 0.0}
        print(f"Added {shares} shares of {ticker} to portfolio.")
        
    def remove_stock(self, ticker, shares):
        if ticker in self.portfolio:
            if shares >= self.portfolio[ticker]['shares']:
                del self.portfolio[ticker]
                print(f"Removed all shares of {ticker} from portfolio.")
            else:
                self.portfolio[ticker]['shares'] -= shares
                print(f"Removed {shares} shares of {ticker} from portfolio.")
        else:
            print(f"Stock {ticker} not found in portfolio.")

    def fetch_stock_price(self, ticker):
        API_KEY = "your_api_key_here"  # Replace with a valid API key
        URL = f"https://api.example.com/stock/{ticker}/price" # Replace with actual API endpoint
        
        try:
            response = requests.get(URL, params={"apikey": API_KEY})
            response.raise_for_status()
            data = response.json()
            return data['price']
        except requests.exceptions.RequestException as e:
            print(f"Error fetching price for {ticker}: {e}")
            return None

    def update_prices(self):
        for ticker in self.portfolio:
            price = self.fetch_stock_price(ticker)
            if price is not None:
                self.portfolio[ticker]['price'] = price

    def display_portfolio(self):
        print("\nPortfolio:")
        print("Ticker\tShares\tPrice\tValue")
        print("---------------------------------")
        total_value = 0
        for ticker, data in self.portfolio.items():
            value = data['shares'] * data['price']
            total_value += value
            print(f"{ticker}\t{data['shares']}\t${data['price']:.2f}\t${value:.2f}")
        print("---------------------------------")
        print(f"Total Portfolio Value: ${total_value:.2f}")

if __name__ == "__main__":
    portfolio = StockPortfolio()
    
    while True:
        print("\nOptions:")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Update stock prices")
        print("4. Display portfolio")
        print("5. Exit")
        
        choice = input("Enter your choice:2 ")
        
        if choice == "1":
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(ticker, shares)
        elif choice == "2":
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(ticker, shares)
        elif choice == "3":
            portfolio.update_prices()
            print("Stock prices updated.")
        elif choice == "4":
            portfolio.display_portfolio()
        elif choice == "5":
            print("Exiting portfolio tracker.")
            break
        else:
            print("Invalid choice. Please try again.")
