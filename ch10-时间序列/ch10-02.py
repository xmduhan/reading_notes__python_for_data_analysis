# -*- coding: utf-8 -*-

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                       1   
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#%%
import pandas as pd

#%%
p = pd.Period('2007',freq='A-DEC')
#%%
p.asfreq(freq='M',how='start')
#%%
p.asfreq(freq='M',how='end')
#%%
p = pd.Period('2007',freq='A-JUN')
#%%
p.asfreq(freq='M',how='start')
#%%
p.asfreq(freq='M',how='end')
#%%