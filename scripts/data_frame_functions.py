#!/opt/anaconda3/bin/python3
# -*- coding: utf-8 -*- 

import sys
sys.path.insert(1, 'scripts')
import pandas as pd
import numpy as np
import directory_functions
import file_management_functions
import string_transformation_functions.py
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk  


def loadDataFrame(csv_exist=bool):
    if (csv_exist == True):
        df = pd.read_csv('data/preprocessed_data/blog_df.csv', parse_dates=['Date'], header=0, names=['Date', 'Post', 'Id', 'Sex', 'Age', 'Theme', 'Sign'])
    else:
        df = createDataFrameFromScratch()
    return df

def loadData(long_str, path, txt_exist=bool):
    if (txt_exist == True):
        with open(r'data/preprocessed_data/no_stops_list.txt', 'r') as file:
            no_stops = []
            for line in file:
                file_text = file.readline()
                no_stops.append(file_text.strip())
            file.close()
    else:
        # Tokenize the article: tokens
        long_str_theme = long_str
        tokens = word_tokenize(long_str_theme)

        # Convert the tokens into lowercase: lower_tokens
        lower_tokens = [t.lower() for t in tokens]
        nltk.download('stopwords')
        english_stops = stopwords.words("english")

        # Retain alphabetic words: alpha_only
        alpha_only = [t for t in lower_tokens if t.isalpha()]

        # Remove all stop words: no_stops
        no_stops = [t for t in alpha_only if t not in english_stops]
        directory_functions.goToMainDirectory(path)
        with open(r'data/preprocessed_data/no_stops_list.txt', 'a') as write_file:
            for word in no_stops:
                write_file.write(str(word) + '\n')
            write_file.close()
    return no_stops


def createDataFrameFromScratch():
    directory_functions.goToWorkingDirectory()
    file_management_functions.createFileOfFiles('listf.txt')
    file_list = file_management_functions.getFileList('listf.txt')
    df_all_data_list = [file_management_functions.load_xml(file) for file in file_list]
    df_all_data = concatenateDataFrames(df_all_data_list, axis=0, ignore_index=True)
    df_all_data.columns = ['Date', 'Post', 'Id', 'Sex', 'Age', 'Theme', 'Sign']
    df_all_data['Date'] = string_transformation_functions.objectToDatetime(df_all_data, 'Date')
    df_all_data.set_index('Date', inplace=True) 
    df_all_data.to_csv(r'../preprocessed_data/blog_df.csv', index = True)
    return df_all_data

def createDataFrame(**df_dict):
    df = pd.DataFrame(df_dict)
    return df

def fillColumnsWithDataFromFileName(title_data, df):
    df_id = createDataFrame()
    for col in range (len(title_data)):
         df_id[col] = pd.Series([title_data[col]] * df.shape[0])
    return df_id 

def concatenateDataFrames(df_list=list, axis=None, ignore_index=None):
    df_all= pd.concat(df_list, axis=axis, ignore_index=ignore_index)
    return df_all

def getFullDf(title_data, **df_dict):
    df1 = createDataFrame(**df_dict)
    df2 = fillColumnsWithDataFromFileName(title_data, df1)
    df_all = concatenateDataFrames([df1, df2], axis=1)
    return df_all


