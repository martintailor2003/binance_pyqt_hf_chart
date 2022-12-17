
import mplfinance as mpf
import matplotlib.pyplot as plt
from settings import candles_number
import matplotlib.animation as animation

plt.rcParams['toolbar'] = 'None'

def chart_init():
    style = mpf.make_mpf_style(base_mpf_style='yahoo')
    fig = mpf.figure(style=style, figsize=(10,5))
    ax = fig.add_subplot(1,1,1)
    print("Chart initialized")
    return fig, ax, fig



def chart_replot(df,ax,fig):
    ax.clear()
    mpf.plot(df,ax=ax, type='candle')
    print("Chart plotted")

