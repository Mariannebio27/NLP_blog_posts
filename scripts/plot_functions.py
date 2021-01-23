#!/opt/anaconda3/bin/python3
# -*- coding: utf-8 -*- 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.feature_extraction.text import CountVectorizer

def plot10MostCommonWords(d_count, count_vectorizer):
    words = count_vectorizer.get_feature_names()
    total_counts = np.zeros(len(words))
    for t in d_count:
        total_counts+=t.toarray()[0]
    
    count_dict = (zip(words, total_counts))
    count_dict = sorted(count_dict, key=lambda x:x[1], reverse=True)[0:10]
    words = [w[0] for w in count_dict]
    counts = [w[1] for w in count_dict]
    x_pos = np.arange(len(words)) 

    plt.bar(x_pos, counts, align='center')
    plt.xticks(x_pos, words, rotation=90) 
    plt.xlabel('words')
    plt.ylabel('counts')
    plt.title('10 most common words')
    plt.show()

def combinePlots(x, y, color=None, label=None, xlabel='', ylabel='', title='', fig_size=(15, 10.5), show=None, add_plot=None):
    plt.plot(x, y, color=color, label=label)  
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.title(title, fontsize=16)
    if label!=None:
        plt.legend()
    if (add_plot!=None):
        add_plot
    if (show==None):
        fig = plt.gcf()
        fig.set_size_inches(fig_size)
        plt.show()


def barPlot(data, color=None, rotation=0, xlabel='', ylabel='', title='', hue=None, ax_fontsize=14, title_fontsize=16, fig_size=(15, 10.5), sns_plot=False, **kw):
    if (sns_plot==True):
        ax = sns.barplot(data=data, x=kw['sns_x'], y=kw['sns_y'], hue=hue)
    else:
        ax = data.plot(kind='bar', color=color)
    ax.set_xlabel(xlabel, fontsize=ax_fontsize)
    ax.set_ylabel(ylabel, fontsize=ax_fontsize)
    ax.set_title(title, fontdict={'fontsize': title_fontsize, 'fontweight': 'medium'})
    try:   
        ax.legend(loc=kw['leg_loc'], ncol=kw['leg_ncol'], fontsize=kw['leg_fontsize'])
    except:
        pass
    fig = plt.gcf()
    fig.set_size_inches(fig_size)
    plt.xticks(rotation=rotation)
    plt.show()


def heatMapPlot(crosstab, annot=False,  xlabel='', ylabel='', title='', ax_fontsize=14, title_fontsize=14, fig_size=(15, 10.5)):
    ax = sns.heatmap(crosstab, yticklabels=True, annot=annot, cbar=True) 
    ax.set_xlabel(xlabel, fontsize=ax_fontsize)
    ax.set_ylabel(ylabel, fontsize=ax_fontsize)
    ax.set_title(title, fontdict={'fontsize': title_fontsize, 'fontweight': 'medium'})
    fig = plt.gcf()
    fig.set_size_inches(fig_size)
    plt.show()

