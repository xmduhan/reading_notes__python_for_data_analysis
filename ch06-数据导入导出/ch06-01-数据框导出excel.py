# -*- coding: utf-8 -*-
"""
Created on Thu Mar 06 18:44:24 2014

@author: 管理员
"""
#%%
from pandas import DataFrame
from pandas.io.excel import ExcelWriter

#%% 生成一个测试数据 
data = DataFrame({'a':range(10), 'b':range(10,20), 'c':range(20,30)})
data

#%% 导出到excel
datafile = ExcelWriter(r'c:\test1.xls')
data.to_excel(datafile,'sheet1')
datafile.save()