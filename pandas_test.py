import pandas as pd

nifty = pd.read_csv("pandas_data.csv")
df = pd.DataFrame(nifty).head(20)
print(df[['Date', 'Open', 'High', 'Low', 'Close']])