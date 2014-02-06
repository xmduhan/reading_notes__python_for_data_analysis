# -*- coding: utf-8 -*-

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    对系列元素的增删
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#%%
from pandas import Series
from string import letters
a=Series(range(10),list(letters[:10]))
b=Series(range(10,20),list(letters[10:20]))
#%%  按label进行drop
a.drop('a')
#%%  按position进行drop 前提是label是唯一的
a.drop(a.index[0])
#%%  使用重建索引的方法删除一个指定位置的元素,也要求label是唯一的
a=a.reindex(a.index.delete(0))
#%%  合并两个系列 不会剔除重复相当于union all 
a.append(b)
#%%  为系列增加一个元素
a.append(Series({'z':100}))
#%%  为系列增加一个元素,元素已经存在更新其值
a=a.set_value('x',24)
a=a.set_value('y',25)
a=a.set_value('z',26)
a
#%%  删除重复的值（注意不是删除label重复)
a.append(a).drop_duplicates()
#%% 删除所有空值
a.dropna()

#%%

指定位置删除一个元素
插入一个元素，不产生新的系列，直接在原有系列上增加
如何把一个已有值设置为空值



