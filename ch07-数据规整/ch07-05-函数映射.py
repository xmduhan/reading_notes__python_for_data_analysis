# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                       函数映射   
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#%%
import pandas as pd
from pandas import Series,DataFrame
from string import letters
d=DataFrame({'a':['a','b'] * 5,'b':['pandas','Series','DataFrame','string','import'] * 2})
#%% 使用序列的map映射一个处理函数 
d['b'].map(str.upper)
#%% 如果对应的函数需要额外参数
d['b'].map(lambda x:x.replace('a','*'))
#%% 通过字典做值替换
d['a'].map({'a':1,'b':2})
#%% #如果给值不全会变成空
d['a'].map({'a':1})

#%% 对数据框可以用applymap
d.applymap(len)

#%%


