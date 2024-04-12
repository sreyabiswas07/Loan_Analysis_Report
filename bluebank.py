#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:52:38 2024

@author: sreyabiswas
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#method 1 to read json data

json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data

with open ('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
#transform the file in to dataframe

loandata = pd.DataFrame(data)
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe data of a specific column
loandata['int.rate'].describe()

loandata['fico'].describe()

#using exp() to calculate annual income
income = np.exp(loandata['log.annual.inc'])

#adding income to loandata as a new column
loandata['annual_income'] = income

#creating an array
arr = [1,2,3]

# #FICO score

# fico = 700

# if fico >= 300 and fico < 400:
#     ficocat ='Very Poor'
# elif fico >= 400 and fico < 600:
#     ficocat = 'Poor'
# elif fico >= 601 and fico < 660:
#     ficocat = 'Fair'
# elif fico >= 660 and fico < 780:
#     ficocat = 'Good'
# elif fico >= 780:
#     ficocat = 'Excellent'
# else:
#     ficocat = 'Unknown'
# print(ficocat)    




# if loandata['fico'] >= 300 and loandata['fico'] < 400: 
#     ficocat ='Very Poor'
# elif loandata['fico'] >= 400 and loandata['fico'] < 600: 
#     ficocat = 'Poor' 
# elif loandata['fico'] >= 601 and loandata['fico'] < 660: 
#     ficocat = 'Fair' 
# elif loandata['fico'] >= 660 and loandata['fico'] < 780: 
#     ficocat = 'Good' 
# elif loandata['fico'] >=780: 
#     ficocat = 'Excellent'
# else:
#     ficocat = "Unknown"


#applying for loop on loandata
length = len(loandata)
ficocat = []

for x in range(0,length):
    catagory = loandata['fico'][x]
    
    try:
        if catagory >= 300 and catagory < 400: 
            cat ='Very Poor'
        elif catagory >= 400 and catagory < 600: 
            cat = 'Poor' 
        elif catagory >= 601 and catagory < 660: 
            cat = 'Fair' 
        elif catagory >= 660 and catagory < 700: 
            cat = 'Good' 
        elif catagory >=700: 
            cat = 'Excellent'
        else:
            cat = "Unknown"
    except:
        cat = "Unknown"
        
        
    ficocat.append(cat)
        
ficocat = pd.Series(ficocat)

#adding ficocat to loandata
loandata['fico_catagory'] = ficocat


#creating a new col for interest rate, rate > 0.12 then high, else low
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'



#plotting fico_catagory column
catplot = loandata.groupby(['fico_catagory']).size()
catplot.plot.bar(color = 'green', width =0.1)
plt.show()

#plotting fico_catagory column
purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'pink', width =0.1)
plt.show()

#scatterplot
ypoint = loandata['annual_income']
xpoint = loandata['dti']

plt.scatter(xpoint, ypoint )
plt.show()

#export to a new csv file
loandata.to_csv('bluebank_CleanedFile.csv',index = True)










