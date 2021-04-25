# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 18:00:42 2020

@author: User
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 23:10:38 2020

@author: User
"""


import matplotlib.pyplot as plt
import numpy as np

countries=np.loadtxt('countries.txt',skiprows=1,dtype='str')

indicator=np.loadtxt('indicators.txt',skiprows=1)

GDP=indicator[:,6]

indicators_under_1000=np.where(GDP<1000)

country=countries[:,0]
region=countries[:,1]

europe_countries=country[np.where(region=='Europe')]

europe_data=indicator[np.where(region=='Europe')]



turkey_employment_data_male=indicator[:,7][np.where(country=='Turkey')]
turkey_employment_data_female=indicator[:,8][np.where(country=='Turkey')]

life_expectancy_male=indicator[:,3][np.where(region=='Europe')]
life_expectancy_female=indicator[:,4][np.where(region=='Europe')]

infantMortality=indicator[:,5][indicators_under_1000]

GDP_under_1000=GDP[indicators_under_1000]

plt.figure(1)
plt.clf()

plt.subplot(1,2,1)

plt.bar('Europe Male',np.mean(life_expectancy_male),align='center')
plt.bar('Europe Female',np.mean(life_expectancy_female),align='center')

plt.ylabel('Life Expectancy')
plt.title('Life Expectancy for Europe by Gender')
plt.legend(['Men','Women'])

plt.subplot(1,2,2)
plt.plot(GDP_under_1000,infantMortality,'b--*')

plt.xlabel('GDP')
plt.ylabel('Infant Mortality')
plt.title('Infant Mortality with GDP under 1000')
plt.grid('on')
plt.figure(2)
plt.clf()

plt.subplot(2,1,1)
ratio=[float(turkey_employment_data_male),float(turkey_employment_data_female)]
names=['Male','Female']
exp=[0,0.1]

plt.pie(ratio,explode=exp,labels=names,autopct='%.1f%%')

plt.title('Emploment Rates by Gender in Turkey')

ax=plt.subplot(2,1,2)

fertility=indicator[:,0]
fertility.sort()
data = plt.hist(fertility,4)
ax.set_xticks(np.around(data[1],2))
plt.title('Frequency of Fertility Rates for All Countires (4 bins)')



