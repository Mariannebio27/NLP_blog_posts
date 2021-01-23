#!/opt/anaconda3/bin/python3
# -*- coding: utf-8 -*- 

import pandas as pd
import numpy as np 
import re
import dateparser


def getLongString(df1, groupby_col1, exhibit_col2, theme):
    long_post = df1[df1[groupby_col1] == theme][exhibit_col2]
    long_string = long_post.str.cat(sep = ' ')      
    return long_string

def objectToDatetime(df, column=str):
    df[column] = df[column].map(lambda x: re.sub(',',' ', x))
    no_number = df[column].str.contains('\d', regex=True)
    df.loc[~no_number, column] = np.nan
    df.dropna(inplace = True)
    df[column] = df[column].apply(lambda x: dateparser.parse(x))
    return df[column]
