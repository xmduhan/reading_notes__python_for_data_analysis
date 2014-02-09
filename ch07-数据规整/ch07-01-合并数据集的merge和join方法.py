# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                合并数据集的merge和join方法
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#%%
from pandas import DataFrame
from string import letters
d1 = DataFrame({'a':range(10),'b':range(5) * 2,'c':range(2)*5})
d2 = DataFrame({'a':range(10),'b1':range(5) * 2,'c1':range(2)*5})   
d3 = DataFrame({'a1':range(10),'b':range(5) * 2,'c':range(2)*5})  
d4 = DataFrame({'a':range(10),'b':range(1,6) * 2,'c':range(2)*5})
d5 = DataFrame({'a':range(5),'b':range(5),'c':list(letters[:5])})
d6 = DataFrame({'a':list(letters[:10]),'b':list(letters[:10])})
d7 = d2.set_index(['b1','c1'])
d8 = DataFrame({'d':range(10),'e':range(5) * 2,'f':range(2)*5}) 
d9 = DataFrame({'g':range(10),'h':range(5) * 2,'i':range(2)*5}) 
#%% 如果没有指定关联的列名，则用两个数据相同的列名的列来关联          
d1.merge(d2)
#%% 如果有两个或以上的同名列，会一起用来关联
d1.merge(d3)
#%%
d1.merge(d4)    # Empty!!
#%% 指定关联的列名
d1.merge(d4,on='a')
#%% 指定一组列名做组合关联
d1.merge(d4,on=['a','c'])
#%% 设定后缀
d1.merge(d4,on='a',suffixes=('_d1', '_d4'))  # 不能搞成前缀吗？
#%% 关联方式默认为inner
d1.merge(d5,on='a')
#%% 指定关联方式 
d1.merge(d5,on=['a','b'],how='left')
#left  : left outer join
#right : right outer join
#outer : full outer join                                             
#inner : inner join
#%% 关联的左列名和右列名不一样
d1.merge(d3,left_on='a',right_on='b')
#%% 指定其中一个数据框使用索引关联
d1.merge(d6,left_on='a',right_index=True)
# 这似乎是个bug当一个数据框指定了列名，另一个数据框指定使用索引
# 被指定为关联列的数据在结果集中重复出现
#%% 指定两个数据框都用索引关联
d1.merge(d6,left_index=True,right_index=True)
#%% 指定多列和复合索引进行关联
d1.merge(d7,left_on=['b','c'],right_index=True)

#%%
d1.join(d8)
#%%
d1.join(d8,on='a') 
# join 是有诸多限制的:
# 1、只有主表能够使用列名其他表必须使用索引
# 2、如果主表指定了两个以上的列名，从表必须有复合索引以之对应
# 3、除非指定了lsuffix和rsuffix参数，否则所有数据框中的列名是不能重复的
# 4、默认情况向使用的是left jion 
#%% 指定了lsuffix 或 rsuffix 后列名可以重复
d1.join(d2,rsuffix='_d2') 
#%% 默认外关联
d1.join(d5,rsuffix='_d5')
#%% 可用通过执行指定how实现内部关联
d1.join(d5,how='inner',rsuffix='_d5')
#%% 可是同时关联多个数据框，但这回列名真的不能重复
d1.join([d8,d9])
#%%

'''
总得来说，join限制较多实际使用可能merge会比较常用，比较和数据库的关联来说，pandas的数
据框关联灵活性和方便性是明显的，但是无法多数据框关联是硬伤(虽join可以多数据框关联，但
是要求所有的列名不重复，有点不切实际了)。
'''


