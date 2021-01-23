#!/opt/anaconda3/bin/python3
# -*- coding: utf-8 -*- 

#import numpy as np
#import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer



def printTopicsLDA(model, count_vectorizer, n_words):
    words = count_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        print("\nTopic #%d:" % topic_idx)
        print(" ".join([words[i]
        for i in topic.argsort()[:-n_words - 1:-1]]))


