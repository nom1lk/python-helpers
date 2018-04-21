
# https://www.youtube.com/watch?v=Iqjy9UqKKuo
# https://pythonprogramming.net/data-analysis-python-pandas-tutorial-introduction/

import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.now()

df = web.DataReader("XOM", "morningstar", start, end)

df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

print(df.head())

df['High'].plot()
plt.legend()
plt.show()








# Pandas column accessor:
df.Close

# Pandas access first element of column of dataframe
df.Close[0]



