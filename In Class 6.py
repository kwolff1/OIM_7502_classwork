import requests
import pandas as pd

url = 'https://www.slickcharts.com/sp500/performance'
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
df = pd.read_html(response.text)[0]

df[['#', 'Company', 'Symbol', 'YTD Return']].to_csv("sp500_performance.csv", index=False)

print("Saved to SP500_performance.csv")