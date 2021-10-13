# Importing required modules

import pandas as pd
import numpy as np


#code for Q1

q1=pd.read_csv('./input/question-1/main.csv')
q11=q1.set_index('Year')
q1_ans=q11.drop('Population',axis= 1).groupby((q11.index//10)*10).sum()
population=q11['Population'].groupby((q11.index//10)*10).max()
q1_ans.insert(1,'Population',population)
q1_ans.drop('Total',axis=1,inplace=True)
q1_ans.to_csv('./output/answer-1/main.csv')


#Code for Q2
dataset2=pd.read_csv('./input/question-2/main.csv')
ans2=dataset2.groupby('occupation').age.agg(['min', 'max'])
ans2.to_csv('./output/answer-2/main.csv')

#Code for Q3

dataset3=pd.read_csv('./input/question-3/main.csv')
data3_copy=dataset3[['Team', 'Yellow Cards', 'Red Cards']]
data3_copy.sort_values(by=['Red Cards', 'Yellow Cards'], inplace = True,ascending=False)
data3_copy
data3_copy.to_csv('./output/answer-3/main.csv')