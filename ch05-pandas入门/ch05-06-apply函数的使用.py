# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                 apply函数的使用
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#%%
from pandas import DataFrame,Series
from string import letters
s=Series(range(10),list(letters[:10]))
d=DataFrame(
    {'a':range(0,10),'b':range(10,20),'c':range(20,30)},
    index=list(letters[:10])
)
    
#%% 返回值可是是一个数值
def f1(x):return x.max()
d.apply(f1)

#%% 返回值也可以是一个系列
def f2(x):return Series([x.max(),x.min()],index=[1,2])
d.apply(f2)

#%% 但返回值不能是一个数据框
def f3(x):
    return DataFrame({'a':range(0,10),'b':range(10,20),'c':range(20,30)})
d.apply(f3)

#%% 列表也不行
def f4(x):return [1,2,3]
d.apply(f4)

#%% 可以应用到每一个元素
def f5(x):
    return x%3
d.applymap(f5)

#%% applymap的返回值可以使用列表
def f6(x):
    return [x,x%3]
d.applymap(f6)