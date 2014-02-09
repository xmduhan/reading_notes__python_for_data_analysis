# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                        系列的空值处理
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#%%
from pandas import Series
from string import letters
import pandas as pd
a=Series(repeat(0.0,10),index=list(letters[:10])[::-1])
b=Series(arange(0,10,dtype=np.float64),index=list(letters[:10]))
c=Series(arange(0,10,dtype=np.float64),index=list(letters[:10]))
a[1] = np.nan
a[3] = np.nan
a[5] = np.nan
c[3:8] = np.nan
#%%
a
#%%
b
#%%
c

#%% 空值检查
a.isnull()
#%%
a.notnull()
#%% 直接删除系列中的空值
a.dropna()
#%%
a.fillna(-1)
#%%
a.fillna(b)           # 这里要十分小心，虽然我们给fillna一个索引完全一致只是顺序不
                      # 同的系列，但它是实际还是当成list来处理了，即通过位置进行空值
                      # 填充而不是使用索引来对齐
#%% pad / ffill: 前值填充 
c.fillna(method='ffill')
#%% backfill / bfill: 后值填充
c.fillna(method='bfill')
#%% 限定填充范围 
c.fillna(method='ffill',limit=2).fillna(method='bfill',limit=2)

#%% np中的where，其实这个函数的功能远比空值处理来的多
np.where(a.isnull(),0,a)
#%% 是基于位置的，没有基于索引，np自然是不了解pandas中的索引
np.where(a.isnull(),b,a)
#%% 还可以写成
np.where(a.notnull(),a,b)   # 这样逻辑会比上一个语句来得清晰
#%% 基于索引的空值填充
a.combine_first(b)
# np.where 是基于位置计算，pd.combine_first是基于索引计算

