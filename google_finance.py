import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

"""
過去2年のデータから翌週を予想する
"""

TRAIN_DAYS = 600
TEST_DAYS = 7

train_start = datetime.datetime(2010, 1, 1)
train_end = train_start+datetime.timedelta(days=TRAIN_DAYS)
test_start = train_end+datetime.timedelta(days=1)
test_end = test_start+datetime.timedelta(days=TEST_DAYS)

train = web.DataReader("F", 'google', train_start, train_end)
test = web.DataReader("F", 'google', test_start, test_end)

"""
単純移動平均
r1,r2,r3,
         p1,
   r2,r3,p1,
            p2
"""
start = train[-20:].Close.data
test_list = [i for i in start]
for i in range(TEST_DAYS):
    test_list.append(sum(test_list)/len(test_list))
    test_list.pop(0)
print(test_list)
plt.plot(train.Close)
plt.plot(test.Close)
plt.show()
