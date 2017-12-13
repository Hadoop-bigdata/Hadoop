#! /usr/bin/env python

#import package
import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def mapper():
    
    analyzer = SentimentIntensityAnalyzer()

    for line in sys.stdin:
        data = eval(line.strip())
        rate = data['overall']
        summary = data['reviewText']
        #summary = data['result']
        vs = analyzer.polarity_scores(summary)
        vs['rate'] = rate
        print(vs)
mapper()
