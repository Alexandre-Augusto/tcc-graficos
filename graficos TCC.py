#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker

dadosAC = pd.read_excel('C:/Users/alexa/Desktop/ntransformado.xlsx', 'AC')
dadosAC

dadosFDI = pd.read_excel('C:/Users/alexa/Desktop/ntransformado.xlsx', 'FDI')
dadosFDI

fig, ax = plt.subplots(3, 2)


# In[2]:


SeteTresAC = dadosAC[['Ano', 'SeteTresAC']]
SeteTresAC.rename(columns={'SeteTresAC': 'Índice'})
SeteTresAC = SeteTresAC.rename(columns={'SeteTresAC': 'Índice'})
fig, ax = plt.subplots()
plt.rcParams['figure.figsize'] = [15.0, 4.50]
#x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
#y = SeteTresAC['Índice']

SeteTresAC['Ano'] = SeteTresAC['Ano'].astype('int32')

x = SeteTresAC['Ano']
x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
y = SeteTresAC['Índice']
plt.xticks(x)
SeteTresAC.plot('Ano', 'Índice')

ax.plot(x, y)
plt.show


# In[3]:


SeteDoisAC = dadosAC[['Ano', 'SeteDoisAC']]
SeteDoisAC = dadosAC[['Ano', 'SeteDoisAC']]
SeteDoisAC.rename(columns={'SeteDoisAC': 'Índice'})
SeteDoisAC = SeteDoisAC.rename(columns={'SeteDoisAC': 'Índice'})
fig, ax = plt.subplots()
plt.rcParams['figure.figsize'] = [15.0, 4.50]
#x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
#y = SeteDoisAC['Índice']

SeteDoisAC['Ano'] = SeteDoisAC['Ano'].astype('int32')

x = SeteDoisAC['Ano']
x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
y = SeteDoisAC['Índice']
plt.xticks(x)
#SeteDoisAC.plot('Ano', 'Índice')

ax.plot(x, y)
plt.show


# In[4]:


SeteTresFDI = dadosFDI[['Ano', 'SeteTresFDI']]
SeteTresFDI.rename(columns={'SeteTresFDI': 'Índice'})
SeteTresFDI = SeteTresFDI.rename(columns={'SeteTresFDI': 'Índice'})
fig, ax = plt.subplots()
plt.rcParams['figure.figsize'] = [15.0, 4.50]
#x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
#y = SeteTresFDI['Índice']

SeteTresFDI['Ano'] = SeteTresFDI['Ano'].astype('int32')

x = SeteTresFDI['Ano']
x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y = SeteTresFDI['Índice']
plt.xticks(x)
#SeteTresFDI.plot('Ano', 'Índice')

ax.plot(x, y)
plt.show


# In[5]:


SeteDoisFDI = dadosFDI[['Ano', 'SeteDoisFDI']]
SeteDoisFDI.rename(columns={'SeteDoisFDI': 'Índice'})
SeteDoisFDI = SeteDoisFDI.rename(columns={'SeteDoisFDI': 'Índice'})
fig, ax = plt.subplots()
plt.rcParams['figure.figsize'] = [15.0, 4.50]
#x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
#y = SeteDoisFDI['Índice']

SeteDoisFDI['Ano'] = SeteDoisFDI['Ano'].astype('int32')

x = SeteDoisFDI['Ano']
x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y = SeteDoisFDI['Índice']
plt.xticks(x)
#SeteDoisFDI.plot('Ano', 'Índice')

ax.plot(x, y)
plt.show


# In[6]:


OitoTres = dadosFDI[['Ano', 'OitoTres']]
OitoTres.rename(columns={'OitoTres': 'Índice'})
OitoTres = OitoTres.rename(columns={'OitoTres': 'Índice'})
fig, ax = plt.subplots()
plt.rcParams['figure.figsize'] = [15.0, 4.50]
#x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
#y = OitoTres['Índice']

OitoTres['Ano'] = OitoTres['Ano'].astype('int32')

x = OitoTres['Ano']
x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y = OitoTres['Índice']
plt.xticks(x)
#OitoTres.plot('Ano', 'Índice')

ax.plot(x, y)
plt.show


# In[7]:


OitoDois = dadosFDI[['Ano', 'OitoDois']]
OitoDois.rename(columns={'OitoDois': 'Índice'})
OitoDois = OitoDois.rename(columns={'OitoDois': 'Índice'})
fig, ax = plt.subplots()
plt.rcParams['figure.figsize'] = [15.0, 4.50]
#x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
#y = OitoDois['Índice']

OitoDois['Ano'] = OitoDois['Ano'].astype('int32')

x = OitoDois['Ano']
x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y = OitoDois['Índice']
plt.xticks(x)
#OitoDois.plot('Ano', 'Índice')

ax.plot(x, y)
plt.show


# In[24]:


lista


# In[25]:


lista = [  ['AAAAAAAAAAAA',
            'BBBBBBBBBBBB'],
         ['CCCCCCCCCCCC',
          'DDDDDDDDDDDD'],
         ['EEEEEEEEEEEE',
          'FFFFFFFFFFFF']  ]
lista[0][1]


# In[8]:


#ldaçjlaskdlaskjdasla
SeteTresAC = dadosAC[['Ano', 'SeteTresAC']]
SeteTresAC.rename(columns={'SeteTresAC': 'Índice'})
SeteTresAC = SeteTresAC.rename(columns={'SeteTresAC': 'Índice'})
#fig, ax = plt.subplots()
#x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
#y = SeteTresAC['Índice']

SeteTresAC['Ano'] = SeteTresAC['Ano'].astype('int32')

x1 = SeteTresAC['Ano']
x1 = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
y1 = SeteTresAC['Índice']
#---------------------------------------------------------------------------------------------------------------------
SeteDoisAC = dadosAC[['Ano', 'SeteDoisAC']]
SeteDoisAC = dadosAC[['Ano', 'SeteDoisAC']]
SeteDoisAC.rename(columns={'SeteDoisAC': 'Índice'})
SeteDoisAC = SeteDoisAC.rename(columns={'SeteDoisAC': 'Índice'})

#x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
#y = SeteDoisAC['Índice']

SeteDoisAC['Ano'] = SeteDoisAC['Ano'].astype('int32')

x2 = SeteDoisAC['Ano']
x2 = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
y2 = SeteDoisAC['Índice']
#---------------------------------------------------------------------------------------------------------------------
SeteTresFDI = dadosFDI[['Ano', 'SeteTresFDI']]
SeteTresFDI.rename(columns={'SeteTresFDI': 'Índice'})
SeteTresFDI = SeteTresFDI.rename(columns={'SeteTresFDI': 'Índice'})
#fig, ax = plt.subplots()
#plt.rcParams['figure.figsize'] = [15.0, 4.50]
#x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
#y = SeteTresFDI['Índice']

SeteTresFDI['Ano'] = SeteTresFDI['Ano'].astype('int32')

x3 = SeteTresFDI['Ano']
x3 = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y3 = SeteTresFDI['Índice']

#---------------------------------------------------------------------------------------------------------------------

SeteDoisFDI = dadosFDI[['Ano', 'SeteDoisFDI']]
SeteDoisFDI.rename(columns={'SeteDoisFDI': 'Índice'})
SeteDoisFDI = SeteDoisFDI.rename(columns={'SeteDoisFDI': 'Índice'})
#fig, ax = plt.subplots()
#plt.rcParams['figure.figsize'] = [15.0, 4.50]
#x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
#y = SeteDoisFDI['Índice']

SeteDoisFDI['Ano'] = SeteDoisFDI['Ano'].astype('int32')

x4 = SeteDoisFDI['Ano']
x4 = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y4 = SeteDoisFDI['Índice']

#---------------------------------------------------------------------------------------------------------------------

OitoTres = dadosFDI[['Ano', 'OitoTres']]
OitoTres.rename(columns={'OitoTres': 'Índice'})
OitoTres = OitoTres.rename(columns={'OitoTres': 'Índice'})
#fig, ax = plt.subplots()
#plt.rcParams['figure.figsize'] = [15.0, 4.50]
#x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
#y = OitoTres['Índice']

OitoTres['Ano'] = OitoTres['Ano'].astype('int32')

x5 = OitoTres['Ano']
x5 = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y5 = OitoTres['Índice']
#---------------------------------------------------------------------------------------------------------------------


OitoDois = dadosFDI[['Ano', 'OitoDois']]
OitoDois.rename(columns={'OitoDois': 'Índice'})
OitoDois = OitoDois.rename(columns={'OitoDois': 'Índice'})
#fig, ax = plt.subplots()
#plt.rcParams['figure.figsize'] = [15.0, 4.50]
#x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
#y = OitoDois['Índice']

OitoDois['Ano'] = OitoDois['Ano'].astype('int32')

x6 = OitoDois['Ano']
x6 = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y6 = OitoDois['Índice']



'''y1 = SeteTresAC['Índice']
y2 = SeteDoisAC['Índice']
y3 = SeteTresFDI['Índice']
y4 = SeteDoisFDI['Índice']
y5 = OitoTres['Índice']
y6 = OitoDois['Índice']'''


# In[ ]:


x1


# In[ ]:


teste = pd.to_datetime(x1)
teste.year


# In[ ]:


x1mod = pd.Series(x1)
x1mod


# In[9]:


x1m = np.array(x1)
x2m = np.array(x2)
x3m = np.array(x3)
x4m = np.array(x4)
x5m = np.array(x5)
x6m = np.array(x6)

x1mod = pd.to_datetime(x1m.astype(str), format='%Y')
x2mod = pd.to_datetime(x2m.astype(str), format='%Y')
x3mod = pd.to_datetime(x3m.astype(str), format='%Y')
x4mod = pd.to_datetime(x4m.astype(str), format='%Y')
x5mod = pd.to_datetime(x5m.astype(str), format='%Y')
x6mod = pd.to_datetime(x6m.astype(str), format='%Y')

x1mod


# In[19]:


fig, axs = plt.subplots(nrows=3, ncols=2, constrained_layout=True, figsize=(20, 18))

import matplotlib.transforms as mtransforms

#locator = matplotlib.ticker.MultipleLocator(2)
#plt.gca().xaxis.set_major_locator(locator)
#formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
#plt.gca().xaxis.set_major_formatter(formatter)

#fig.locator_params(integer=True)

x = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
     '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']


axs[0, 0].plot(x1mod, y1, label=r'$Primeira\ Especificação\ (1)$', color='Blue')
axs[0, 1].plot(x2mod, y2, label=r'$Segunda\ Especificação\ (2)$', color='Blue')
axs[1, 0].plot(x3mod, y3, label=r'$Terceira\ Especificação\ (3)$', color='Blue')
axs[1, 1].plot(x4mod, y4, label=r'$Quarta\ Especificação\ (4)$', color='Blue')
axs[2, 0].plot(x5mod, y5, label=r'$Quinta\ Especificação\ (5)$', color='Blue')
axs[2, 1].plot(x6mod, y6, label=r'$Sexta\ Especificação\ (6)$', color='Blue')


#axs[0, 1].text(0.2, 0.5, 'HAHAHA')

#y1 = SeteTresAC['Índice']
#y2 = SeteDoisAC['Índice']
#y3 = SeteTresFDI['Índice']
#y4 = SeteDoisFDI['Índice']
#y5 = OitoTres['Índice']
#y6 = OitoDois['Índice']

#plt.tick_params(bottom=False)

#for ax in axs:
#    ax.tick_params(bottom=False)

#plt.tight_layout()

for i in range(3):
    for j in range(2):
        axs[i, j].tick_params(bottom=False)
        axs[i, j].set_yticks([50, 75, 100, 125, 150])
        axs[i, j].legend(loc='upper left', handlelength=0, handletextpad=0, fontsize=18)
        axs[i, j].axhline(75, color='gray', linestyle='--', alpha=0.3)
        axs[i, j].axhline(100, color='gray', linestyle='--', alpha=0.3)
        axs[i, j].axhline(125, color='gray', linestyle='--', alpha=0.3)
        axs[i, j].axhline(150, color='gray', linestyle='--', alpha=0.3)
        axs[i, j].spines['top'].set_visible(False)
        axs[i, j].spines['right'].set_visible(False)
        #axs[i, j].tick_params(labelrotation=30, axis='x')
        axs[i, j].set_ylabel(r'$Índice$', fontsize=20)
       # axs[i, j].xlim(2002, 2020)
        axs[i, j].tick_params(labelsize=20)
        
        #dá certo mas n tem pq colocar texto
        #axs[i, j].text(0.5, 0.5, 'LALALA', transform=axs[i,j].transAxes)
        #falar que nas duas especificações vai até o 2020 e nas outras até o 2019



plt.savefig('C:/Users/alexa/Desktop/imagenzinha11', dpi=250)


#axs[0, 1].tick_params(bottom=False)

#axs[1, 0].yticks([75, 100, 125])

#axs[0, 0].set_yticks([75, 100,  125, 150])


#axs[0, 1].legend(loc='upper left')

#plt.xticks(rotation=45)


# In[ ]:


y1 = SeteTresAC['Índice']
y2 = SeteDoisAC['Índice']
y3 = SeteTresFDI['Índice']
y4 = SeteDoisFDI['Índice']
y5 = OitoTres['Índice']
y6 = OitoDois['Índice']


# In[ ]:




