# -*- coding: utf-8 -*-

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    数据框数据访问的基本方法
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#%% 
from pandas import DataFrame
from string import letters
d = DataFrame(
    {'a':range(0,10),'b':range(10,20),'c':range(20,30)},
    index=list(letters[:10])
)
d1 = DataFrame(
    {'a':range(0,10),'b':range(10,20),'c':range(20,30)}
)
#%%
d[0]          # error 
#%% 
d['a']        # Series,列
#%%
d[['a','c']]  # DataFrame，列
#%%
d[:5]         # DataFrame，行
#%% 
d.ix[:5]      # position-based，行
#%%
d1.ix[:5]     # label-based，行
#%%           
d.irow(0)     # Series
#%% 
d.icol(0)     # Series
#%%
d.get_value('e','a')    # get_value(row_name,col_name)
#%% 强制使用位置来访问元素的方法
d.iget_value(0,1)       # iget_value(irow,icol)  

#%% 使用条件过滤
d[d>5]
#%% 
d[d.a>5]
#%%
d[(d>5)&(d%3==0)]

#%% 使用条件过滤的本质
d>5       # DataFrame
#%%       
d.a>5     # Series
#%% 可以自己构造一个Series
d[Series(repeat(True,10),index=list(letters[:10]))]
#%% 
d[Series(repeat([True,False],5),index=list(letters[:10]))]
#%% Series长度超过可以 
d[Series(repeat(True,20),index=list(letters[:20]))]
#%% Series长度不够不行
d[Series(repeat(True,5),index=list(letters[:5]))]

