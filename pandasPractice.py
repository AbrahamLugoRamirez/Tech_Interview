
"""
Second Part: Create your code.

In this module you should implement a code that reads the file
nba.xlsx (taken from https://www.geeksforgeeks.org/python-pandas-dataframe/)
and import it as a pandas dataframe and process it.

There should be functions or methods that:

0) Read and import excel file into pandas dataframe (df)
1) Prints the df
2) Return a df with a single given column from the original df
3) Return a list or array (explain choise) from a given column
4) Return a sub-dataframe filtered by a column value
5) Return the merge of two dataframes (you can use the nba2.xlsx)
   with an inner join.
6) Output a given dataframe to an excel file.


Third Part: Challenge yourself
            Implement a simple API in Django with a storage
            in Postgresql that uses the methods for processing
            developed with pandas.
"""

import pandas as pd
import numpy as np
import glob
#df = pd.read_excel('nba.xlsx', sheet_name='nba')

def addData(files: str) -> list:
        allCsv = []
        for file in files:
            temp = open(file, 'r', encoding='utf-8')
            tempDf = pd.read_excel(temp)
            allCsv.append(tempDf)
            
        return allCsv
     
def makeListOfDataFrames(list_of_dataframes):
    auxiliar_list = []
    len_of_dataframes = len(list_of_dataframes[0])
    for i in range(len_of_dataframes):
        dt = pd.DataFrame(list_of_dataframes[0][i])
        auxiliar_list.append(dt)
    return auxiliar_list

def joinDataFrames(dataframes):
    return pd.concat(dataframes)
