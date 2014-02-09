# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                 数据框和向量的计算规则
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#%%
from pandas import DataFrame,Series
from string import letters
s1=Series(range(3),list(letters[:3]))
d1=DataFrame(
    {'a':range(0,3)},
    index=list(letters[:3])
)
d2=DataFrame(
    {'a':range(0,10),'b':range(10,20),'c':range(20,30)},
    index=list(letters[:10])
)

#%%  数据框相加使用的是对齐计算同位置元素
d1+d2
#%%  数据框和系列相加是按列对齐计算同位置元素，并按行扩展
d2+s1
#%% 使用add函数实现按行对齐
#axis表示用哪个label来对齐，而不是广播的方向
d2.add(s1,axis=0)  #  {0, 1, 'index', 'columns'} 
#%%
d2.add(s1,axis=1)


