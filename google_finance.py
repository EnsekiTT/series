import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

train_start = datetime.datetime(2010, 1, 1)
train_end = datetime.datetime(2013, 12, 31)

test_start = datetime.datetime(2014, 1, 1)
test_end = datetime.datetime(2014, 12, 31)

f = web.DataReader("F", 'google', train_start, train_end)
v = web.DataReader("F", 'google', test_start, test_end)

plt.plot(f.Close)
plt.plot(v.Close)
plt.show()
