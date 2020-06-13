#!/usr/bin/env python
# coding: utf-8

# In[42]:


import os
import pandas as pd
import matplotlib as plt
import seaborn as sns

df2 = pd.read_csv("/Users/anikhash/Desktop/Sarma.csv", low_memory=False)
df2.head(10)
df2.dropna(how='any')

#Sarma dataframe, note there is no pita, no soup, no rice as these are common mandatory item sides and will skew data for analysis if left uncleaned

# CODE FOR ALL ROWS DISPLAYED 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


df2 = df2.replace(to_replace =':', value = '', regex = True) 
df2 = df2.replace(to_replace ='Salads & Sides', value = '', regex = True) 
df2 = df2.replace(to_replace ='Hot Meza - Appetizers', value = '', regex = True) 
df2 = df2.replace(to_replace ='Meza - Appetizers', value = '', regex = True) 
df2 = df2.replace(to_replace ='Vegetarian & Seafood Entree Plates ', value = '', regex = True) 
df2 = df2.replace(to_replace ='Kebab Entree by the Pound', value = '', regex = True) 
df2 = df2.replace(to_replace ='Kebabs Entree Plates', value = '', regex = True) 
df2 = df2.replace(to_replace ='Choose Second Side Sub', value = '', regex = True) 
df2 = df2.replace(to_replace ='Specialties Entree Plates', value = '', regex = True) 
df2 = df2.replace(to_replace ='Desserts', value = '', regex = True) 
df2 = df2.replace(to_replace ='Choose First Side', value = '', regex = True) 
df2 = df2.replace(to_replace ='Choose Second Side', value = '', regex = True) 

df2 = df2.replace(to_replace ='Choose Second Kebab', value = '', regex = True) 
df2 = df2.replace(to_replace ='Choose First Kebab', value = '', regex = True) 
df2 = df2.replace(to_replace ='Wraps & Sandwiches', value = '', regex = True) 
df2 = df2.replace(to_replace ='Specialty Entree by the Pound', value = '', regex = True) 


#Clean data strip
df2['Combo']= df2['Combo'].str.strip()

#Line for all counts
df2.groupby('Combo')['Combo'].count().sort_values(ascending=False)

#Import apriori rules

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

basket = (df2[df2['Order Type'] =="Delivery"]
          .groupby(['Order', 'Combo'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('Order'))
    
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
frequent_itemsets = apriori(basket_sets, min_support=0.04, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

rules[ (rules['lift'] >= 6) &
       (rules['confidence'] >= 0.8) ]

#from IPython.display import display, HTML
#display(HTML(rules.to_html()))

sarma = df2.groupby('Combo')['Combo'].count().sort_values(ascending=False)
#Sarma dataframe, no pita, no soup, no rice

import os
import pandas as pd
import matplotlib as plt
import seaborn as sns

df2 = pd.read_csv("/Users/anikhash/Desktop/Sarma.csv", low_memory=False)
df2.head(10)
df2.dropna(how='any')


# CODE FOR ALL ROWS DISPLAYED 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


df2 = df2.replace(to_replace =':', value = '', regex = True) 
df2 = df2.replace(to_replace ='Salads & Sides', value = '', regex = True) 
df2 = df2.replace(to_replace ='Hot Meza - Appetizers', value = '', regex = True) 
df2 = df2.replace(to_replace ='Meza - Appetizers', value = '', regex = True) 
df2 = df2.replace(to_replace ='Vegetarian & Seafood Entree Plates ', value = '', regex = True) 
df2 = df2.replace(to_replace ='Kebab Entree by the Pound', value = '', regex = True) 
df2 = df2.replace(to_replace ='Kebabs Entree Plates', value = '', regex = True) 
df2 = df2.replace(to_replace ='Choose Second Side Sub', value = '', regex = True) 
df2 = df2.replace(to_replace ='Specialties Entree Plates', value = '', regex = True) 
df2 = df2.replace(to_replace ='Desserts', value = '', regex = True) 
df2 = df2.replace(to_replace ='Choose First Side', value = '', regex = True) 
df2 = df2.replace(to_replace ='Choose Second Side', value = '', regex = True) 

df2 = df2.replace(to_replace ='Choose Second Kebab', value = '', regex = True) 
df2 = df2.replace(to_replace ='Choose First Kebab', value = '', regex = True) 
df2 = df2.replace(to_replace ='Wraps & Sandwiches', value = '', regex = True) 
df2 = df2.replace(to_replace ='Specialty Entree by the Pound', value = '', regex = True) 


#Clean data strip
df2['Combo']= df2['Combo'].str.strip()

#Line for all counts
df2.groupby('Combo')['Combo'].count().sort_values(ascending=False)

#Import apriori rules

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

basket = (df2[df2['Order Type'] =="Delivery"]
          .groupby(['Order', 'Combo'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('Order'))
    
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
frequent_itemsets = apriori(basket_sets, min_support=0.04, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

rules[ (rules['lift'] >= 6) &
       (rules['confidence'] >= 0.8) ]

#from IPython.display import display, HTML
#display(HTML(rules.to_html()))

sarma = df2.groupby('Combo')['Combo'].count().sort_values(ascending=False)
display(item_counts)
display(item_counts)


# In[41]:


#Kebab dataframe, where pita, lentil, rice etc is included


import os
import pandas as pd
import matplotlib as plt
import seaborn as sns

df3 = pd.read_csv("/Users/anikhash/Desktop/Kebab.csv", low_memory=False)

# CODE FOR ALL ROWS DISPLAYED 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

#First 10 rows displayed
df3.head(10)

# Drop rows with any NaN in the selected columns only
df3.dropna(how='any')

#Let's try dropping specific strings, including utensils, missing, notes
df3= df3[~df3.Combo.str.contains("0 x Set of utensils")]
df3= df3[~df3.Combo.str.contains("1 x Set of utensils")]
df3= df3[~df3.Combo.str.contains("2 x Set of utensils")]
df3= df3[~df3.Combo.str.contains("3 x Set of utensils")]
df3= df3[~df3.Combo.str.contains("4 x Set of utensils")]
df3= df3[~df3.Combo.str.contains("8 x Set of utensils")]

df3= df3[~df3.Combo.str.contains("None")]
df3=df3[~df3.Combo.str.contains("Yes")]
df3=df3[~df3.Combo.str.contains('Missing Item(s)')]
df3=df3[~df3.Combo.str.contains("Missing Order")]

df3=df3[~df3.Combo.str.contains("Food Quality Wrong Preparation")]
df3=df3[~df3.Combo.str.contains("Order Received Partially Damaged")]
df3=df3[~df3.Combo.str.contains("Received Wrong Item")]

df3=df3[~df3.Combo.str.contains("Customer Received Wrong Item Modifier")]
df3=df3[~df3.Combo.str.contains("Order was Late")]
df3=df3[~df3.Combo.str.contains("Missing Item(s)")]

#Also drop the following
#Food Quality Wrong Preparation
#3 x Set of utensils
#Notes: BOTH SIDES OF GARLIC)

#Drop the 'Choose First Side:'
#Drop ' 0x Set of utensils
#Drop ' None
#Drop ' Order Received Partially Damaged
# Received Wrong Item
# Customer Received Wrong Item Modifier
# Order was Late


#Maybe with regex, drop the categories with the : following, i.e. Desserts: 
# Choose First Side:
# Choose Second Side: 
#Kebab Entree by the Pound:
#Hot Meza - Appetizers:
#Wrap & Sandwiches
#Salads & Sides: 
#Make it with:


#Drop the modifications

df3=df3[~df3.Combo.str.contains("Make it with Khash-Khash Style")]
df3=df3[~df3.Combo.str.contains("Make it with Yogurt Style")]

df3=df3[~df3.Combo.str.contains("Pita")]

#Drop rows 206-210 - MISSING ORDER
#df2=df2.drop([206,207, 208, 209, 210])

#from IPython.display import display, HTML
#display(HTML(df2.to_html()))

#df2.columns

#Magic line for all counts
df3.groupby('Combo')['Combo'].count().sort_values(ascending=False)

#Drop Rice, Soup,

df3['Combo']= df3['Combo'].str.strip()


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

basket = (df3[df3['Order Type'] =="Delivery"]
          .groupby(['Order', 'Combo'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('Order'))
    
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
frequent_itemsets = apriori(basket_sets, min_support=0.07, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)


rules[ (rules['lift'] >= 6) &
       (rules['confidence'] >= 0.8) ]


#from IPython.display import display, HTML
#display(HTML(rules.to_html()))

item_counts = df3.groupby('Combo')['Combo'].count().sort_values(ascending=False)
display(item_counts)


# In[65]:


#Pre-covid Postmates dataset

import os
import pandas as pd
import matplotlib as plt
import seaborn as sns

before = pd.read_csv("/Users/anikhash/Desktop/NoPita_Pre.csv", low_memory=False)
df2.head(10)
df2.dropna(how='any')


# CODE FOR ALL ROWS DISPLAYED 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


df2 = df2.replace(to_replace =':', value = '', regex = True) 
df2 = df2.replace(to_replace ='Salads & Sides', value = '', regex = True) 
df2 = df2.replace(to_replace ='Hot Meza - Appetizers', value = '', regex = True) 
df2 = df2.replace(to_replace ='Meza - Appetizers', value = '', regex = True) 
df2 = df2.replace(to_replace ='Vegetarian & Seafood Entree Plates ', value = '', regex = True) 
df2 = df2.replace(to_replace ='Kebab Entree by the Pound', value = '', regex = True) 
df2 = df2.replace(to_replace ='Kebabs Entree Plates', value = '', regex = True) 
df2 = df2.replace(to_replace ='Choose Second Side Sub', value = '', regex = True) 
df2 = df2.replace(to_replace ='Specialties Entree Plates', value = '', regex = True) 
df2 = df2.replace(to_replace ='Desserts', value = '', regex = True) 
df2 = df2.replace(to_replace ='Choose First Side', value = '', regex = True) 
df2 = df2.replace(to_replace ='Choose Second Side', value = '', regex = True) 

df2 = df2.replace(to_replace ='Choose Second Kebab', value = '', regex = True) 
df2 = df2.replace(to_replace ='Choose First Kebab', value = '', regex = True) 
df2 = df2.replace(to_replace ='Wraps & Sandwiches', value = '', regex = True) 
df2 = df2.replace(to_replace ='Specialty Entree by the Pound', value = '', regex = True) 


#Clean data strip
df2['Combo']= df2['Combo'].str.strip()

#Line for all counts
df2.groupby('Combo')['Combo'].count().sort_values(ascending=False)

#Import apriori rules

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

basket = (df2[df2['Order Type'] =="Delivery"]
          .groupby(['Order', 'Combo'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('Order'))
    
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
frequent_itemsets = apriori(basket_sets, min_support=0.04, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

rules[ (rules['lift'] >= 6) &
       (rules['confidence'] >= 0.8) ]

from IPython.display import display, HTML
display(HTML(rules.to_html()))

pre_clean = df2.groupby('Combo')['Combo'].count().sort_values(ascending=False)
display(pre_clean)


# In[32]:


#New sales data to merge
import os
import pandas as pd
import matplotlib as plt
import seaborn as sns

df = pd.read_csv("/Users/anikhash/Desktop/New.csv")

# CODE FOR ALL ROWS DISPLAYED 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

#2 ways to drop a column
#df=df.drop(['Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30'], axis=1)
df=df.drop(columns=['Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30'])

df["Combo"] = df[['items', 'Items_2',
       'Items_3', 'Items_4', 'Items_5', 'Items_6', 'Items_7', 'Items_8',
       'Items_9', 'Items_10', 'Items_11', 'Items_12', 'Items_13', 'Items_14',
       'Items_15', 'Items_16', 'Items_17', 'Items_18', 
       'Items_19','Items_20','Items_21','Items_22','Items_23','Items_24']].values.tolist()

from itertools import zip_longest, product

def xplode(df, explode, zipped=True):
    method = zip_longest if zipped else product

    rest = {*df} - {*explode}

    zipped = zip(zip(*map(df.get, rest)), zip(*map(df.get, explode)))
    tups = [tup + exploded
     for tup, pre in zipped
     for exploded in method(*pre)]

    return pd.DataFrame(tups, columns=[*rest, *explode])[[*df]]

df = xplode(df, ['Combo'], zipped=False)[["Order", "Date", "Order Type", "Combo"]]

df = df.replace(to_replace =':', value = '', regex = True) 
df = df.replace(to_replace ='Salads & Sides', value = '', regex = True) 
df = df.replace(to_replace ='Hot Meza - Appetizers', value = '', regex = True) 
df = df.replace(to_replace ='Meza - Appetizers', value = '', regex = True) 
df = df.replace(to_replace ='Cold Appetizers', value = '', regex = True) 

df = df.replace(to_replace ='Vegetarian & Seafood Entree Plates ', value = '', regex = True) 
df = df.replace(to_replace ='Kebab Entree by the Pound', value = '', regex = True) 
df = df.replace(to_replace ='Kebabs Entree Plates', value = '', regex = True) 
df = df.replace(to_replace ='Choose Second Side Sub', value = '', regex = True) 
df = df.replace(to_replace ='Specialties Entree Plates', value = '', regex = True) 
df = df.replace(to_replace ='Desserts', value = '', regex = True) 
df = df.replace(to_replace ='Choose First Side', value = '', regex = True) 
df = df.replace(to_replace ='Choose Second Side', value = '', regex = True) 

df = df.replace(to_replace ='Choose Second Kebab', value = '', regex = True) 
df = df.replace(to_replace ='Choose First Kebab', value = '', regex = True) 
df = df.replace(to_replace ='Wraps & Sandwiches', value = '', regex = True) 
df = df.replace(to_replace ='Specialty Entree by the Pound', value = '', regex = True) 
df = df.replace(to_replace ='None', value = '', regex = True) 


#Clean data strip
df2['Combo']= df2['Combo'].str.strip()

df.groupby('Combo')['Combo'].count().sort_values(ascending=False)

#Drop
df=df.dropna()
#df.dropna()
#Head
df.head(10)

#Ani figure out how to drop blank rows

#Export CSV

df.columns

import tkinter as tk
from tkinter import filedialog
from pandas import DataFrame

cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]
        }

df = DataFrame(df, columns= ['Order', 'Date', 'Order Type', 'Combo'])


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

def exportCSV ():
    global df
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = False, header=True)

saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButton_CSV)

root.mainloop()


# In[35]:


#ANI: for new orders, add in quantity column, clean data, add to Sarma CSV, then do ML

#New sales data to merge
import os
import pandas as pd
import matplotlib as plt
import seaborn as sns

df = pd.read_csv("/Users/anikhash/Desktop/PlzWork.csv")

# CODE FOR ALL ROWS DISPLAYED 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)



df = df.replace(to_replace ='Vegetarian & Seafood Plates', value = '', regex = True) 
df = df.replace(to_replace ='Kebab Entree Plates', value = '', regex = True) 
df = df.replace(to_replace ='Kebabs Entree Plates', value = '', regex = True) 
df = df.replace(to_replace ='Hot Appetizers', value = '', regex = True) 
df = df.replace(to_replace ='Sandwiches', value = '', regex = True) 
df = df.replace(to_replace ='Specialty Entree Plates', value = '', regex = True) 
df = df.replace(to_replace ='Choose Entree', value = '', regex = True) 
df = df.replace(to_replace ='Specialty Entree Plates ', value = '', regex = True) 


#Clean data strip
#df2['Combo']= df2['Combo'].str.strip()

#df.groupby('Combo')['Combo'].count().sort_values(ascending=False)

#Drop
df=df.dropna()
#df.dropna()
#Head
#df.head(10)

#Ani figure out how to drop blank rows

#Export CSV

#df.columns

import tkinter as tk
from tkinter import filedialog
from pandas import DataFrame

df = DataFrame(df, columns= ['Order', 'Date', 'Order Type', 'Combo','Quantity'])


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

def exportCSV ():
    global df
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = False, header=True)

saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButton_CSV)

root.mainloop()


# In[47]:


#Pre-covid Postmates dataset as Before dataframe

import os
import pandas as pd
import matplotlib as plt
import seaborn as sns

df = pd.read_csv("/Users/anikhash/Desktop/MaySarma.csv", low_memory=False)


# CODE FOR ALL ROWS DISPLAYED 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

#Import apriori rules

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

basket = (df[df['Order Type'] =="Delivery"]
          .groupby(['Order', 'Combo'])['Quant']
          .sum().unstack().reset_index().fillna(0)
          .set_index('Order'))
    
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
frequent_itemsets = apriori(basket_sets, min_support=0.03, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

rules[ (rules['lift'] >= 7) &
       (rules['confidence'] >= 0.7) ]

from IPython.display import display, HTML
display(HTML(rules.to_html()))


# In[ ]:




