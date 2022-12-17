import ccxt, time
import sys
from datetime import datetime
import mplfinance as mpf
from chart import chart_init, chart_replot
from settings import symbol, exchange_name, candles_number, secret_k, api_k
from dataframe_operation import df_init , update_dataframe
import matplotlib.animation as animation

class main():
    def __init__(self):
        print('Initializing...')
        if exchange_name == "binance_futures":
            self.exchange = ccxt.binanceusdm({
                'options': {'adjustForTimeDifference': True,},
                'enableRateLimit': True,
                'apiKey': api_k,
                'secret': secret_k,
            })
        
        else:
            print("Error: invalid exchange name")
            sys.exit()
        self.df_var_bundle = df_init()
        self.fig, self.ax0, self.fig = chart_init()
        
        
    def app(self, ival):
    
        self.df_var_bundle = update_dataframe(self.exchange, self.df_var_bundle)
        df = self.df_var_bundle[0]
        delay = self.df_var_bundle[2]
        #print(df)
        
        
        chart_replot(df=df, ax=self.ax0, fig=self.fig)
            
        #limit the df length
        print(df.pipe(len))
        if df.pipe(len) > candles_number:
            df = df.iloc[1: , :]
            
        print("a")
        
        #ani.event_source.interval *= 3
        #time.sleep(delay)
        print("delay")
    
    
    
    def start_app(self):
        ani = animation.FuncAnimation(self.fig, self.app, interval=10,repeat_delay=1000,repeat=True)
        mpf.show()



if __name__ == "__main__":
    print('Start app')
    ap = main()
    ap.start_app()
    






