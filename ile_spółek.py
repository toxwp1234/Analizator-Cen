import yfinance as yf
import pandas as pd
t :int = 0
def get_sp500_tickers():
    """Fetches the list of S&P 500 companies and their tickers."""
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    table = pd.read_html(url)
    df = table[0]
    return df['Symbol'].tolist()

def count_positive_stocks(tickers):
    """Counts how many stocks are positive today."""
    positive_count = 0
    global t
    for ticker in tickers:
        t+=1
        print(t)
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="1d")
            
            if len(data) > 0:
                open_price = data['Open'][0]
                close_price = data['Close'][0]

                if close_price > open_price:
                    positive_count += 1
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")

    return positive_count

def main():
    print("Fetching S&P 500 tickers...")
    tickers = get_sp500_tickers()
    print(f"Total tickers fetched: {len(tickers)}")

    print("Counting positive stocks...")
    positive_count = count_positive_stocks(tickers)

    print(f"Number of positive stocks today: {positive_count}")

if __name__ == "__main__":
    main()
print(f"Zeskanowano {t} elementów")