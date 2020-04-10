import pandas
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import pandas_datareader as pdr

class SMAC : 
    def __init__(self , equity_of , dt_o , dt_c ,shortwindow = 10 , longwindow = 50 )  :
        self.bars = pdr.get_data_yahoo(equity_of, dt_o , dt_c)
        self.sw = shortwindow
        self.lw = longwindow
        self.signals = None

    def generate_signal(self):
        self.signals = pd.DataFrame(index=self.bars.index)
        self.signals['short_mavg'] = pd.Series(self.bars['Close']).rolling(self.sw).mean()
        self.signals['long_mavg'] = pd.Series(self.bars['Close']).rolling(self.lw).mean()
        plt.legend(loc="upper left")

    def disp(self):
        assert self.signals is not None , "MA not calculated , function not called"
        plt.plot(self.bars['Close'] , label = "equity")
        plt.plot(self.signals['short_mavg'], label = "short moving average")
        plt.plot(self.signals['long_mavg'] , label ="long moving average" )
        plt.legend(loc="upper left")
        plt.show()
        

if __name__ == "__main__":
    dt_o  = datetime.datetime(2019,1,1)
    dt_c = datetime.datetime(2020,1,1)  
    equity_of = 'AAPL'
    obj =SMAC(equity_of  , dt_o  , dt_c) 
    obj.generate_signal()
    obj.disp()
