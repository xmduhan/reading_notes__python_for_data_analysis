# -*- coding: utf-8 -*-


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    系列数据访问的基本方法
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#%% 系列的访问
from pandas import Series
from string import letters
a=Series(range(10),list(letters[:10]))
#%%  使用元素位置访问元素
a[0]         #元素
#%%  使用index访问元素 
a['a']       #元素
#%%  使用切片过滤系列
a[0:5:2]     #系列
#%%  使用索引切片(如果索引非数字其切片是闭区间)
a['b':'i':2]  #系列
#%%  使用布尔值系列进行过滤
a[(a>5)&(a<9)]   #系列
#%%  使用reindex函数
a.reindex(list(letters[5:15]))    #系列
#%%  使用get_value,set_vavlue访问
a.set_value('a',2)   # 元素
a.get_value('a')     # 元素
#%%  使用iget_value访问
a.iget_value(0)      # 元素
#%%  使用get访问
a.get('c')           # 元素
#%%  使用iget访问
a.iget(0)            # 元素
#%%  使用truncate
a.truncate(5,9)      # 系列
#%%  使用item访问      
a.item(9)            # 元素
a.itemset(9,100)     # 元素



#%%
a.idxmax()
#%%
a.idxmin()
