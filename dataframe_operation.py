import  time
import pandas as pd
from settings import symbol, timeframe



def df_init():
    
    #delay
    delay = timeframe/1000
    df = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close','Volume','Spread','Timestamp'])
    previous_time = (time.time() * 1000) - timeframe
    return df, previous_time, delay
    


def update_dataframe(exchange,bundle):
    df, previous_time, delay = bundle
    #fetching trades for 
    trades = exchange.fetch_trades(symbol=symbol, since=previous_time)
    print(trades)
    time_i =  previous_time + timeframe
    print(trades)
    #fatc ob for spread
    orderbook = exchange.fetch_order_book(symbol,limit=20)
    all_bids = orderbook['bids']
    all_asks = orderbook['asks']
    a = 0
    b = 0
    s_list = []
    for x in range(len(all_asks)):
        a = all_asks[x][0]
        b = all_bids[x][0]
        s = a/b
        s_list.append(s)
    spread = sum(s_list) / len(s_list) -1
        
        
    previous_time = time_i
    
    #get trades prices
    prices = []
    qtys = 0
    for x in  trades:
        var0 = x['info']['p']
        var1 = x['info']['q']
        prices.append(var0)
        qtys = qtys + float(var1)
    print(prices)
    date = time.strftime(('%Y-%m-%d %H:%M:%S'),time.localtime(time_i/1000))
    open = float(prices[0])
    high = float(max(prices))
    low = float(min(prices))
    close = float( prices[-1])
    volume = qtys * (float(open)+float(close))/2
    spread = float(spread)

    #add data to the dataframe
    df2 = pd.DataFrame(data = {'Date': [date], 'Open':[open], 'High':[high], 'Low':[low], 'Close':[close], 'Volume':volume, 'Spread':[spread], 'Timestamp':[time_i]})
    df2.index = pd.DatetimeIndex(df2['Date'])
    df = pd.concat([df,df2])       

    return df, previous_time, delay
    