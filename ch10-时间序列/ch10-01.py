# -*- coding: utf-8 -*-
"""
Created on Sun Mar 02 18:31:32 2014

@author: 14F
"""
#%%
from datetime import datetime

#%% 获取当前系统时间
now = datetime.now()


#%% # 时间的拆解
#获取年份
now.year
#%% 获取年的月序
now.month
#%% 获取月的天序
now.day
#%% 获取周的天序
now.weekday()
#%% 获取日期部分
now.date()


#%% 时间的构造和间隔计算
d1 = datetime(2003,1,1)
d1
#%%
d2 = datetime(2014,1,1,11,0)
d2
#%% 注意1为8万秒
delta1 = d2-d1
delta1
#%%
delta1.days
#%%
delta1.seconds
#%%
delta2 = d1-d2
delta2
#%%
delta2.days
#%%
delta2.seconds