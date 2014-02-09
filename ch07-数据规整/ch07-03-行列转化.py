# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                       行列转化   
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#%%
import pandas as pd
from pandas import Series,DataFrame
from string import letters
d1=DataFrame(
    {
        'foo':['one']*3+['two']*3,
        'bar':['a','b','c'] * 2,
        'value1':range(6),
        'value2':range(6,12),
        'value3':range(12,18)
    },
    columns=['foo','bar','value1','value2','value3']
)
d2=d1.set_index(['foo','bar']).unstack('bar')
d3=pd.concat([d1,d1])
#%% d1.pivot(行,列,值)    
d1.pivot('foo','bar','value1')
#%% 
d1.pivot('foo','bar',['value1','value2'])  # error
# 这是为什么要报错的呢？
#%% 只能用一下语句实现上面的功能
d1.pivot('foo','bar')[['value1','value2']]
#%% 保留所有的列
d1.pivot('foo','bar')
# pivot单纯只是对数据实现行转列的功能，里面的数据是没有经过计算的
# pivot实际上是将行值设置为索引，然后再用unstack转化到列中
#%% 这里的用set_index和unstack实现和pivot等效功能
d1.set_index(['foo','bar']).unstack('bar')

#%%
d2
#%% 列索引转化为行索引
d2=d2.stack()
d2
#%% 行索引转化为列索引
d2=d2.unstack()
d2

#%% pivot_talbe不是行列转化函数，是分组聚集函数，放在这里只是希望区别pivot函数
# 这是在做分组求和
d3.pivot_table('value1',rows='bar',cols='foo',aggfunc=sum) 
#%%
# 由于有重复不能做pivot操作
d3.pivot('foo','bar','value1')     # error

#%% 将行数据转化为列名
d4=d1.set_index([d1.index,'foo']).unstack()
d4
#%% 将列名转化为行数据
d4=d4.swaplevel(0,1,axis=1).stack()
d4.set_index(d4.index.droplevel(0)).reset_index()
#%% 交换数据框的横
# DataFrame.swapaxes(axis1, axis2, copy=True) 
# axis = 0 表示行，axis = 0 表示列，真不明白这个函数为啥需要这两个参数
# d1.swapaxes(0,1) 和 d1.swapaxes(1,0) 都管用
d1.swapaxes(0,1)

#%%
'''
我们通常指的行转列是把一整列的数据（也就是一整列中的所有行）转化到一级列名上，也可以把
一级列名转化到一个数据列上去（列转行），但似乎却无法直接将一级行索引转化成一行数据，这
说明pandas的行列操作也不是完全平衡的。当然在使用swapaxes后就可以了,当然这种操作奇怪得
很，估计是很难用到的。以下演示了这样的转化
'''
#%% 将一整列的数据转化为一整行 
d6=d1.set_index([d1.index,'foo']).unstack()
d6.swapaxes(0,1).reset_index().set_index('level_0').swapaxes(0,1)
#%%
'''
这里涉及到一个数据分析处理的惯性思维的问题：我们通常要求一列的数据是同一种类型，而很少
要求一行的数据是同一种类型。所以在看到这种奇怪的数据转换，比较难以理解且说明白其代表的
含义
'''










