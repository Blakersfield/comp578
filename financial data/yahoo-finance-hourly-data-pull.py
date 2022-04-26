import pandas as pd
import yfinance as yf

# hourly price of apple for last 6mo
"""
^GSPC     =     S&P 500
^DJI      =     Dow Jones Industrial Average
^IXIC     =     NASDAQ
GC=F      =     Gold
SI=F      =     Silver
BTC-USD   =     Bitcoin in USD
PA=F      =     Palladium
RUB=X     =     USD to Ruble
UAH=X     =     USD to Hryvnia
"""
stock_ticker = {'S&P': '^GSPC', 'DowJones': '^DJI', 'NASDAQ': '^IXIC', 
                'Gold': 'GC=F', 'Silver': 'SI=F', 'Bitcoin': 'BTC-USD',
                'Palladium': 'PA=F', 'Ruble': 'RUB=X', 'Hryvnia': 'UAH=X'}

stock_keys = list(stock_ticker.keys())

for key in stock_keys:
    dataframe = yf.download(tickers=stock_ticker[key], period = "6mo", interval="60m")

    # Adjust filepath to desired location
    dirname = 'C:\\Users\\casas\\Desktop\\COMP 578\\Project\\Financial Data\\'
    filename = str(key)+'.csv'
    filepath = dirname + filename

    # Create dummy csv file
    with open(filepath, 'w') as f:
        f.write('text')

    dataframe.to_csv(filepath)
    
    # Separate Datetime field into two separate fields Date and Time
    data = pd.read_csv(filepath)

    temp = []
    date = []
    time = []
    
    for i in range(len(data)):
        temp.append(str(data.iloc[i][0]).split(' '))
        date.append(temp[i][0])
        time.append(temp[i][1])

    data.drop('Datetime', axis=1, inplace=True)
    data.insert(0, "Time", time, True)
    data.insert(0, "Date", date, True)
    
    # Index=False removes index numbering
    data.to_csv(filepath, index=False)