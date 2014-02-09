# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                合并数据集的concat方法
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#%%
import pandas as pd
from pandas import Series,DataFrame
s1=Series(range(5))
s2=Series(range(5,10))
s3=Series(range(10))
d1 = DataFrame({'a':range(10),'b':range(10,20),'c':range(20,30)})
d2 = DataFrame({'a':range(30,40),'b':range(40,50),'c':range(50,60)})
d3 = DataFrame({'a':range(10),'b':range(10),'c':range(10)},index=range(1,11))

#%% 使用concat在行方向上合并数据,即类似数据库的union
pd.concat([s1,s2,s3])
#%% 合并后重编索引
pd.concat([s1,s2,s3],ignore_index=True)
#%%
pd.concat([s1,s2,s3],ignore_index=True).reindex(range(15))
#%% 
pd.concat([s1,s2,s3],ignore_index=True).reindex(range(25))
#%% 合并数据时为行设置上级索引,以区分数据
pd.concat([s1,s2,s3],keys=['s1','s2','s3'])

#%% 使用concat在列方向上进行合并数据，
#   类似merge，但是使用concat的就只能用索引来合并数据了
pd.concat([s1,s2,s3],axis=1)
#%% 合并的同时，重新设定行索引
pd.concat([s1,s2,s3],axis=1,join_axes=[range(8)])
#%% 合并的同时，为列取名字
pd.concat([s1,s2,s3],axis=1,keys=['s1','s2','s3'])
#%% 对于数据框的合并指定keys会形成一个上级的索引 
pd.concat([d1,d2],axis=1,keys=['d1','d2'])
#%% 也可以通过传入一个字典的方式，实现以上功能
pd.concat({'d1':d1,'d2':d2},axis=1)
#%% 也可以对数据框进行按行合并
pd.concat({'d1':d1,'d2':d2})
#%% concat默认情况使用outer,而且是完全外连接
pd.concat({'d1':d1,'d3':d3},axis=1)
#%% 通过指定join='inner'来进行内部连接
pd.concat({'d1':d1,'d3':d3},axis=1,join='inner')