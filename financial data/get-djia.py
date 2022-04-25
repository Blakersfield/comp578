import pandas as pd
import yfinance as yf

# hourly price of apple for last 6mo
dataframe = yf.download(tickers="YM=F", period = "6mo", interval="60m")
dataframe.to_csv('test.csv')

data = pd.read_csv('test.csv')

temp = data
print(type(temp))

tempt = []
for i in range(len(temp)):
    tempt.append(str(temp.iloc[i][0]).split(' '))

date = []
time = []

for i in range(len(tempt)):
    date.append(tempt[i][0])
    time.append(tempt[i][1])

temp.drop('Datetime', axis=1, inplace=True)
temp.insert(0, "Time", time, True)
temp.insert(0, "Date", date, True)
temp.to_csv('test.csv')

