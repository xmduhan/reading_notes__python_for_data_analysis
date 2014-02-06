# -*- coding: utf-8 -*-


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
         整型下标的label-based和position-based规则 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#%%  下标问题
from pandas import Series
from string import letters
a=Series(range(10),list(letters[:10]))
b=Series(range(10))
c=Series(range(10),range(5,15))

#label-based   切片运算使用的是开区间
#positon-based 切片运算使用的是闭区间

#%% (1) a[n] 如果label是整型则使用label-based,否则使用position-based
a[100]     # IndexError, position-based
#%%
b[100]     # KeyError, label-based 
#%%
c[100]     # KeyError, label-based 

#%% (2) a[:5]    positon-based 
a[:3]     # position-based 
#%%
b[:3]     # 开区间说明是 position-based
#%%
c[:3]     # label是不存在的，说明使用的是position-based
#%%  
c[:12]    # 如果是label-based，应该在12就停止,所以是position-based 

#%% (3) a.ix[n]  如果label是整型则使用label-based,否则使用position-based
a.ix[0]   # posotion-based
#%%
b.ix[0]   # label-based
#%%
c.ix[0]   # label-based

#%% (3) a.ix[:n] 如果label是整型则使用label-based,否则使用position-based
a.ix[:5]  # posotion-based   
#%% 
b.ix[:5]  # label-based
#%%
c.ix[:5]  # label-based



