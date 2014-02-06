# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                       any和all的用法   
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#%%
import pandas as pd
from pandas import Series,DataFrame
from string import letters
d1 = DataFrame({'a':range(10),'b':range(10,20),'c':range(20,30)})

#%%
d1>25
#%% 于寻找有任意一"行"(按行,axis=0)大于>25的"列"
(d1>25).any()
#%%
d1>25
#%% 于寻找有任意一"列"(按列,axis=1)大于>25的"行"
(d1>25).any(1)

#%%
d1>15
#%% 所有"行"(按行,axis=0)都大于15的列
(d1>15).all()
#%% 
d1>5
#%% 所有"列"(按列,axis=1)都大于5的行
(d1>5).all(1)