# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:01:35 2019

@author: Ara
"""

import pandas as pd
d1 = {'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
d2 = {'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
d3 = {'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
d4 = {'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}

data1 = pd.DataFrame(d1, columns = ['Student','Math'])
data2 = pd.DataFrame(d2, columns = ['Student','Electronics'])
data3 = pd.DataFrame(d3, columns = ['Student','GEAS'])
data4 = pd.DataFrame(d4, columns = ['Student','ESAT'])

m1 = pd.merge(data1,data2,how='left', on='Student')
m2 = pd.merge(data3,data4,how='left', on='Student')
merge = pd.merge(m1,m2,how='left', on='Student')
long = pd.melt(merge,id_vars=['Student'],var_name ='Subject',
               value_name='Grades')

print('Wide Tidy Grades:\n',merge,'\n\n')
print('Long Tidy Grades:\n',long,'\n\n')