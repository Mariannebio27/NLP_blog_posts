#!/opt/anaconda3/bin/python3
# -*- coding: utf-8 -*- 

import sys
sys.path.insert(1, 'scripts')
import os 
import data_frame_functions
import directory_functions
from pathlib import Path
from lxml import objectify

def checkIfFileExists(step, path=None):
    if (step==1):
        if Path('data/preprocessed_data/blog_df.csv').is_file():
            return True
        else:
            return False
    else:
        directory_functions.goToMainDirectory(path)
        if Path('data/preprocessed_data/no_stops_list.txt').is_file():
            return True
        else:
            return False


def parsingXmlToRoot(path):
    parsed = objectify.parse(open(path))                                                        
    root = parsed.getroot()
    return root

def getChildrenValuesFromRoot(root):
    date = []    
    post = [] 
    for child in root.getchildren():
        if child.tag == 'date':
            date.append(child.pyval)
        else:
            post.append(child.pyval)
    return date, post

def stripDataFromFileName(path):
    col_names = path.rsplit('/')[-1].rstrip('.xml').rsplit('.')
    return col_names

def load_xml(file_name):
    try:
        root = parsingXmlToRoot(file_name)
        date, post = getChildrenValuesFromRoot(root)
        file_name_data = stripDataFromFileName(file_name)
        df_dict = {'Date': date, 'Post': post}
        df_all = data_frame_functions.getFullDf(file_name_data, **df_dict)
        return df_all
    except:
        pass

def createFileOfFiles(file):
    if Path(file).is_file():
        os.remove(file)
    listf = os.listdir()
    with open(file, 'w') as new_file:
        for line in listf:
            new_file.write(line + '\n')
    new_file.close()

def getFileList(file):
    with open(file, 'r') as files:
        file_text = files.read()
    file_list = file_text.replace('\n', ' ').split(' ') 
    return file_list


