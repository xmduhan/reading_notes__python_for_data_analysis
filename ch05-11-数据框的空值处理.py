# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    数据框的空值处理
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#%%
from pandas import DataFrame
from string import letters
d = DataFrame(arange(100.0).reshape(10,10),columns=list(letters[:10]))
#%%
d[d%13==0]=np.nan
d[d%17==0]=np.nan
d[(d>=80) & (d<90)]=np.nan
#%%
d
#%% 所有含有空值的行全部删除
d.dropna()
#%% 只删除全部是空值的数据
d.dropna(how='all')
#%% 只要有一列数据为空就删除 
d.dropna(how='any')
#%% 要求至少有9列数据不为空
d.dropna(thresh=9)
#%% 按列进行删除
d.dropna(thresh=8,axis=1)
#%% DataFrame没有isnull方法
d.isnull()
#%% 空值填充
d.fillna(0)
#%% 
d.fillna(dict(zip(letters[:10],range(-1,-11,-1))))
# 注意：使用dropna时默认使用的坐标是行，使用fillna时默认是使用列
#%% 
d.fillna(method='ffill',limit=1)