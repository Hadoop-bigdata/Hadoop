#! /usr/bin/env python

import pandas as pd
import numpy as np
import sys
from sklearn import metrics



pred = []
true = []

for line in sys.stdin:
    
    data = eval(line)
    #print(data)
    
    viewid = data.pop("a")
    p = data.pop("pred")
    t = data.pop("true")

    

    pred.append(p)
    true.append(t)


score = metrics.accuracy_score(true,pred)
matrix = metrics.confusion_matrix(true,pred)
print(score)
print(matrix)
