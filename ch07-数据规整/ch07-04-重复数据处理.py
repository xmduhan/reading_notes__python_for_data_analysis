# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                       重复数据处理   
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#%%
import pandas as pd
from pandas import Series,DataFrame
from string import letters
d1 = DataFrame({'a':['a','b']*6,'b':[1,2,3,4,5,6]*2,'c':[1,3,5]*4})

#%% 列出重复记录
d1.duplicated()
#%% 选择非重复记录
d1[d1.duplicated()==False]
#%% 按列计算重复
d1.duplicated('a')
#%% 按两个以上列
d1.duplicated(['a','c'])
#%% 保留最后一个元素
d1.duplicated('a',take_last=True)

#%% 删除重复 
# drop_duplicates() 等效于执行 d1[d1.duplicated()==False]
d1.drop_duplicates()

