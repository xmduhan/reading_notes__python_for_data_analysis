# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                  非唯一索引和索引修改
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#%%
from pandas import Series
i = [0]*5+[1]*5+[2]
s1 = Series(range(11),index=i)
s2 = Series(range(11))
d1 = DataFrame({'a':range(10),'b':range(10),'c':range(10)})
d2 = DataFrame({'a':range(10),'b':range(10),'c':range(10)})
#%%
# 非唯一索引带来一个比较棘手的问题，就是用下标访问数据时，无法确定返回值是元素还是一个
# 系列，在实际使用的过程中最好能过极力的避免这种情况。 
s1[0]        # 返回Series
#%%
s1[2]        # 返回元素
#%%    判断索引是否是唯一
s1.index.is_unique

#%% 对于行索引可以使用reindex进行重编
s2.reindex(index=range(10,21))
#%% 但对于非唯一性索引这个函数无法用
s1.reindex(range(11))     #error
#%% 只能使用强制索引修改
s1.index=range(11)
# 这样的问题就是他不是产生一个新的数据集，而直接影响原来的数据
#%%
s1

#%% 可以通过放访问和修改index和columns字段 
d2.index
#%% 
d2.index=list(letters[:10])
d2
#%%
d2.columns
#%%
d2.columns = ['d','e','f']
#%%
d2

#%% 当然还可以调用index.map函数
d2.index=d2.index.map(len)
# 这样同样会修改原来的数据集
#%%
d2.columns=d2.columns.map(len)

#%% 通过rename来访对index和columns进行重命名，它可以生成新的数据集，用起来比较方便
# 可以是用函数映射重命名，也可以是用字典替换，其最终的可能都是调用对应的map函数实现的
d1.rename(index=lambda x:'line'+str(x),columns={'a':'d','b':'e','c':'f'})
# 在用rename对index和columns进行重命名的时候，要求命名后的数据不重复

#%%
'''
总结:虽然pandas可以支持重复的数据索引，但是很多的处理函数在索引不唯一的时候都会报错，
无法正常使用，所以能支持重复索引还是为了数据处理的中间过程的特殊需要而预留的，原则上最
好不要出现这种情况
'''

