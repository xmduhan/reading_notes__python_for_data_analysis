# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                       数据离散化处理   
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#%%
import pandas as pd
from pandas import Series,DataFrame
from string import letters
d1 = DataFrame({'a':range(1000),'b':range(1000),'c':range(1000)})
d2 = DataFrame({
    'a':np.random.rand(1000),
    'b':np.random.normal(size=(1000)),
    'c':range(1000)
})

#%% 要求把数据分成10片
a = pd.cut(d1.a,10)
type(a)
# 返回值是pandas.core.categorical.Categorical          
# 这玩意应该类似R语言中的factor对象
#%% 将分片结果保存回DataFrame
d1['a1'] = pd.cut(d1.a,10)
#%% 注意默认情况区间是左开右闭，可以通过传入right=False改变这一特性
pd.cut(d1.a,10,right=False) 
#%% 可以通过传入labels参数为每个桶命名
pd.cut(d1.a,10,labels=list(letters[:10]))
#%% 可以传入人为设定的切分数,注意：要把范围的开头和结尾也传进去 
pd.cut(d1.a,[0,250,500,750,1000],labels=['a','b','c','d'])
#%% 数据分箱默认依据等距规则进行划分
d2['b1']=pd.cut(d2.b,10,labels=list(letters[:10]))
d2.groupby('b1')['b1'].count()
#%% 可以指定分箱数据的精度
d2['b2']=pd.cut(d2.b,10,labels=list(letters[:10]),precision=2)
d2.groupby('b2')['b2'].count()
#%% 可以用qcut对数据做等密度分箱
d2['b3']=pd.qcut(d2.b,10,labels=list(letters[:10]))
d2.groupby('b3')['b3'].count()
#%% qcut可以输入分位数来指定分箱的边界
d2['b4']=pd.qcut(d2.b,[0,.33,.67,1],labels=list(letters[:3]))
d2.groupby('b4')['b4'].count()

#%% pandas中还有一个value_counts()方法可以直接用于计算Categorical的各分类数量
pd.value_counts(pd.qcut(d2.b,[0,.33,.67,1],labels=list(letters[:3])))
