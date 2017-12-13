#! /usr/bin/env python

import pandas as pd
import numpy as np
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

# initialize
rates = []
trains = []

# get each line data
# transfer data to list
for line in sys.stdin:
    rate_data = eval(line)
    rate = rate_data.pop("rate")
    value = rate_data.values()


    # append all the rate and value to form whole list
    rates.append(rate)
    trains.append(value)

# transfer all the data to numpy array
x = np.array(trains)
y = np.array(rates)

# set how many line you want to set as test data
n = 10000
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

# save score as ouput
print(score)
