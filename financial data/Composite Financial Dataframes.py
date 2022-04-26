import pandas as pd
import yfinance as yf

# # # # # # # # # # # # # # # # # # #
# daily prices since January 1, 2022 #
# # # # # # # # # # # # # # # # # # #
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

dirname = 'C:\\Users\\casas\\Desktop\\Financial Data 2\\'
df2filename = 'DailyFinancialDataframe.csv'

df_data = []

i = 0

for key in stock_keys:
    dataframe = yf.download(tickers=stock_ticker[key], start='2022-01-01', 
                            end='2022-04-21', interval="1d")

    filename = str(key)+'.csv'
    filepath = dirname + filename

    with open(filepath, 'w') as f:
        f.write('text')

    dataframe.to_csv(filepath)
    
    temp = pd.read_csv(str(filepath), usecols=['Date', 'High'])
    df_data.append(temp)
    df_data[i].columns = ['Date', stock_keys[i]]
    df_data[i] = df_data[i].set_index('Date', drop=True)
    if (i > 0):
        df_data[0] = df_data[0].join(df_data[i], how='inner')
    i += 1

df_data[0].to_csv(dirname + df2filename)
# # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # #
# hourly prices since January 1, 2022 #
# # # # # # # # # # # # # # # # # # # #
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
                'Silver': 'SI=F', 'Palladium': 'PA=F', 'Gold': 'GC=F',
                'Bitcoin': 'BTC-USD', 'Ruble': 'RUB=X', 'Hryvnia': 'UAH=X'}

stock_keys = list(stock_ticker.keys())

dirname = 'C:\\Users\\casas\\Desktop\\Financial Data 3\\'

df_data = []

i = 0

for key in stock_keys:
    dataframe = yf.download(tickers=stock_ticker[key], start='2022-01-01', 
                            end='2022-04-21', interval="60m")
    
    filename = str(key)+'.csv'
    filepath = dirname + filename

    with open(filepath, 'w') as f:
        f.write('text')

    dataframe.to_csv(filepath)
    
    # Dataframe for S&P 500, DowJones, and NASDAQ (US-NYSE)
    if i <= 2:
        temp = pd.read_csv(str(filepath), usecols=['Datetime', 'High'])
        df_data.append(temp)
        df_data[i].columns = ['Datetime', stock_keys[i]]
        df_data[i] = df_data[i].set_index('Datetime', drop=True)
        if (i > 0):
            df_data[0] = df_data[0].join(df_data[i], how='inner')
    
    # Dataframe for Silver, Gold, and Palladium (Precious Metals)
    elif 2 < i <=5:
        temp = pd.read_csv(str(filepath), usecols=['Datetime', 'High'])
        df_data.append(temp)
        df_data[i].columns = ['Datetime', stock_keys[i]]
        df_data[i] = df_data[i].set_index('Datetime', drop=True)
        if (i > 3):
            df_data[3] = df_data[3].join(df_data[i], how='inner')
   
    # Dataframe for Bitcoin, Ruble, and Hryvnia (Currencies)
    else:
        temp = pd.read_csv(str(filepath), usecols=['Datetime', 'High'])
        df_data.append(temp)
        df_data[i].columns = ['Datetime', stock_keys[i]]
        df_data[i] = df_data[i].set_index('Datetime', drop=True)
        if (i > 6):
            df_data[6] = df_data[6].join(df_data[i], how='inner')
    i += 1

df_data[0].to_csv(dirname + 'USNYSEFinancialDataFrame.csv')
df_data[3].to_csv(dirname + 'PreciousMetalsFinancialDataFrame.csv')
df_data[6].to_csv(dirname + 'CurrencyFinancialDataFrame.csv')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
