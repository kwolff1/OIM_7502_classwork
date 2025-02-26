import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
import yfinance as yf

sb.set_theme()

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())


class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()

    def get_data(self):
        data = yf.download(self.symbol, start=self.start, end=self.end)
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = [col[0] for col in data.columns]
        data.index = pd.DatetimeIndex(data.index)
        self.calc_returns(data)
        return data

    def calc_returns(self, data):
        data["Change"] = data["Close"].diff()
        data["Instant Return"] = np.log(data["Close"]).diff().round(4)

    def plot_return_dist(self):
        plt.hist(self.data["Instant Return"] * 100, bins=30, color="blue", edgecolor="white")
        plt.title(f"Daily Instant Returns {self.symbol.upper()}")
        plt.show()

    def plot_performance(self):
        self.data["Cumulative Return"] = (self.data["Close"] / self.data["Close"].iloc[0]) - 1
        plt.plot(self.data.index, self.data["Cumulative Return"] * 100, color = "blue")
        plt.xlabel("Date")
        plt.ylabel("Cumulative Return (%)")
        plt.title(f"Performance of Stock {self.symbol} from {self.start} to {self.end}")
        plt.show()


def main():
    test = Stock(symbol="MTN", start="2024-01-01", end="2024-12-31")
    print(test.data)

if __name__ == '__main__':
    main()