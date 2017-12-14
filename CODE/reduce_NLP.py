#! /usr/bin/env python

import pandas as pd
import numpy as np
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

def ctrnum(data):
        ctr1 = 0
        ctr2 = 0
        ctr3 = 0
        ctr4 = 0
        ctr5 = 0
        for i in  data:
                if i == 1:
                        ctr1 = ctr1 + 1
                elif i == 2:
                        ctr2 = ctr2 + 1
                elif i == 3:
                        ctr3 = ctr3 + 1
                elif i == 4:
                        ctr4 = ctr4 + 1
                elif i == 5:
                        ctr5 = ctr5 + 1
        return ctr1, ctr2, ctr3, ctr4, ctr5

# initialize
rates = []
trains = []

# set how many line you want to set as test data
n = 10000

# get each line data
# transfer data to list
for line in sys.stdin:
    rate_data = eval(line)
    rate = rate_data.pop("rate")
    viewid = rate_data.pop("account")
    value = rate_data.values()


    # append all the rate and value to form whole list
    rates.append(rate)
    trains.append(value)

# transfer all the data to numpy array
x = np.array(trains)
y = np.array(rates)

# set traning test data base on n
train_x = x[:-n,:]
test_x = x[-n:,:]

train_y = y[:-n]
test_y = y[-n:]


# use random forest to train the data
rf = RandomForestClassifier()
rf.fit(train_x, train_y)

# get predict rate
y_pred = rf.predict(test_x)

# get the accuracy between ture rate and predict rate
score = metrics.accuracy_score(test_y,y_pred)

pred1, pred2, pred3, pred4, pred5 = ctrnum(y_pred)
test1, test2, test3, test4, test5 = ctrnum(test_y)

print("For rating 1, the accuracy is " + format(pred1/test1, '0.3f'))
print("For rating 2, the accuracy is " + format(pred2/test2, '0.3f'))
print("For rating 3, the accuracy is " + format(pred3/test3, '0.3f'))
print("For rating 4, the accuracy is " + format(pred4/test4, '0.3f'))
print("For rating 5, the accuracy is " + format(pred5/test5, '0.3f'))

# save score as ouput
print('The final accurary is'+ format(score, '0.3f')
