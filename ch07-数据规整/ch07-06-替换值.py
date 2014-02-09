# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                       替换值   
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#%%
import pandas as pd
from pandas import Series,DataFrame
from string import letters
d1 = DataFrame({'a':range(10),'b':range(10),'c':range(10)})
d2 = DataFrame({'a':arange(10.),'b':arange(10.),'c':arange(10.)})
d2[:2]=np.nan

#%% 用replace指定替换的值
d1.replace(5,-1)
#%% 对不同的值指定不同的替换值
d1.replace([1,2,3],[-1,-2,-3])
#%% 也是可以实现空值替换的
d2.replace(np.nan,-1)
# 疑问：在一个DataFrame中如果某列是整型如何表示空值呢？
d1.replace({1:-1,2:-2,3:-3})

