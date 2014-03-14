# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                       数据排序
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#%%
from pandas import Series,DataFrame
from string import letters
s1=Series(arange(10,dtype=np.float64),index=list(letters[:10])[::-1])
s1[5]=np.nan
d1=DataFrame(
    {'a':range(10),'b':repeat([0,1],5),'c':repeat([0,1,2,3,4],2)},
    index=list(letters[:10])
)
d2=d1.set_index([d1.index,d1['b']])
d2.index.names=['r0','r1']

#%%
s1.order()
#%%
s1.order(ascending=False)
#%%
s1.order(na_last=False)
#%%
s1.sort_index()

#%% 对于数据框没有order这个方法
d1.order()     # error
#%% 按索引排序
d1.sort_index()
#%% 按字段排序
d1.sort(['b', 'c'], ascending=[1, 0])
#%%
d1.sort(['c', 'b'], ascending=[1, 0])
#%% sort_index功能可以覆盖sort
d1.sort_index(by='c',ascending=False)
#%%
d1.sort_index(by=['b','c'],ascending=[0,1])

#%% 对列名排序
d1.sort_index(axis=1,ascending=False)
#%% 对列指定出现的顺序
d1[['c','b','a']]

#%% 如果想根据某一行数据对列进行排序 
d1.reindex(columns=d1.ix['j'].order().index)

#%% 指定行顺序的排序
d1.ix[['b','c','a']]

#%% 根据多级索引进行排序
d2.sortlevel(0,ascending=False)
#%%
d2.sortlevel(0,ascending=False).sortlevel(1)

#%% 对元素进行排名
d1.rank()
#%% 指定是用相同值最小的排名、倒叙
d1.rank(method='min',ascending=False)
