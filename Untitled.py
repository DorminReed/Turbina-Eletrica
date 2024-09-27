#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


# In[42]:


turbina = pd.read_csv('T1.csv')
turbina.columns = ['Data/Hora', 'Potência(KW)', 'VelocidadeDoVento(m/s)', 'CurvaTeórica(KW)', 'DireçãoDoVento(°)']
del turbina['DireçãoDoVento(°)']
turbina['Data/Hora'] = pd.to_datetime(turbina['Data/Hora'], format= "mixed")
display(turbina)


# In[45]:


sns.scatterplot(data=turbina, x='VelocidadeDoVento(m/s)', y='Potência(KW)')


# In[ ]:





# In[47]:


sns.scatterplot(data=turbina, x='VelocidadeDoVento(m/s)', y='CurvaTeórica(KW)')


# In[58]:


pot_real = turbina['Potência(KW)'].tolist()
pot_teorica =  turbina['CurvaTeórica(KW)'].tolist()
print(pot_real[0:15])
pot_maxima = []
pot_minima = []
dentro_limite = []

for potencia in pot_teorica:
    pot_maxima.append(potencia*1.05)
    pot_minima.append(potencia*0.95)

for p, potencia in enumerate(pot_real):
    if potencia>= pot_minima[p] and potencia<= pot_maxima[p]:
        dentro_limite.append('Dentro')
    elif potencia == 0:
        dentro_limite.append('Zero')
    else:
        dentro_limite.append('Fora')

print(dentro_limite.count('Dentro')/len(dentro_limite))
        


# In[62]:


turbina['DentroLimite'] = dentro_limite
display(turbina)


# In[72]:


cores = {'Dentro':'blue', 'Fora':'red', 'Zero':'orange'}
sns.scatterplot(data=turbina, x='VelocidadeDoVento(m/s)', y='Potência(KW)', hue='DentroLimite', s=1, palette = cores)

