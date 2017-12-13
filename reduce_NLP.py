#! /usr/bin/env python

import pandas as pd
import numpy as np
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics


key = []
train = []

for line in sys.stdin:
    rate_data = eval(line)
    rate = rate_data.pop("rate")
    value = rate_data.values()



    key.append(rate)
    train.append(value)


x = np.array(train)
y = np.array(key)


n = -10000
train_x = x[:n,:]
test_x = x[n:,:]

train_y = y[:n]
test_y = y[n:]


# train
rf = RandomForestClassifier()
rf.fit(train_x, train_y)
y_pred = rf.predict(test_x)
score = metrics.accuracy_score(test_y,y_pred)
print(score)
