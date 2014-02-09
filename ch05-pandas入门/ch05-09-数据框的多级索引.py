# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                        数据框的多级索引
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#%%
from pandas import DataFrame
from string import letters
d = DataFrame(
    np.arange(16).reshape(4,4),
    index=[['c','c','d','d'],['c1','c2','d1','d2']],
    columns=[['a','a','b','b'],['a1','a2','b1','b2']]
)
#%%
d['a']
#%%
d[:3]
#%%
d[::-1]
#%%
d['a','a1']
#%%
d[:,'a1']            # 对于多级系列这样的操作是可以的，但对于数据框则行不通

#%% 对数据多级索引起名字
d.index.names = ['row1','row2']
d.columns.names = ['col1','col2']
d
#%% 交换行索引的级别
d.swaplevel(0,1)
#%%
d.swaplevel('row1','row2')
#%% 交换列索引顺序 
d.swaplevel(0,1,axis=1)

#%% 将行索引的最低一级转化为列索引 
d.unstack()
#%% 将列索引的最低一级转化为行索引
d.stack()
# 疑问:
# d.stack().stack() 变成一个系列是可以理解的，但为何d.unstack().unstack() 
# 也变成一个系列了

#%% 互换行和列
d.swapaxes(0,1)

# 将索引转化为列
d1=d.reset_index()
d1

#%% 将列转化为索引
d1.set_index('row1')
#%% 转化后保留列
d1.set_index('row1',drop=False)
#%% 将两个列转化为索引
d1.set_index(['row1','row2'])
#%% 如果列名和索引名称重复，会失败
d1.set_index('row1',drop=False).reset_index()
#%% 重命名即可解决
d2=d1.set_index('row1',drop=False)
d2.index.names=['r1']
d2.reset_index()
#%% 将列为多重索引情况下的转行索引
d3=d2.reset_index()
d3.set_index([('a','a1')])
# 疑问:不能直接将行转化为列索引吗?


