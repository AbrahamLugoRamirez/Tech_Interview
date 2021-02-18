
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

"""
Abraham Lugo Ramirez
Ingeniero de sistemas y computación
3005608510
labrahamdedios@gmail.com
"""

"Import libraries"
import pandas as pd
import numpy as np


class data():
   def __init__(self):
      """Reading excel file"""
      """Point 0"""
      self.df = pd.read_excel('nba.xlsx', sheet_name='nba')
      self.df2 = pd.read_excel('nba2.xlsx', sheet_name='nba')
      
   def point1(self):
      """Prints dataframes"""
      print(self.df)
      print(self.df2)


   def point2(self, columna):
      """Returns a dataframe with a single column given to the original dataframe"""
      dataframe = self.df[columna].to_frame()   
      return dataframe
 
   def point3(self):
      """Name column List, In case I want to iterate"""
      dataframe = self.df['Name'].values.tolist()
      return dataframe
 
   def point4(self):
      """sub-dataframe filtered by a column value,  where Team ==Boston Celtics"""
      dataframe = self.df.loc[self.df['Team'] == "Boston Celtics"]
      return dataframe
   
   def point5(self):
      """merge of two dataframes with an inner join."""
      dataframe = pd.merge(self.df, self.df2, how="inner", on='Name')
      return dataframe
   
   def point6(self):
      dataframe = self.df.loc[self.df['Team'] == "Boston Celtics"]
      #dataframe = point4()
      dataframe.to_excel("output.xlsx")
     
   
   #dff = pd.concat(df)


if __name__ == '__main__':
   datos = data()
   datos.point1()
   df2 = datos.point2('Name')
   df3 = datos.point3()
   df4 = datos.point4()
   df5 = datos.point5()
   datos.point6()
 
