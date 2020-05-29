# -*- coding: utf-8 -*-
"""
Created on Tue May 26 10:56:30 2020

@author: isabe
"""
from jaratoolbox import loadbehavior
#from jaratoolbox import extraplots
#import numpy as np
import matplotlib.pyplot as plt 
#from statsmodels.stats.proportion import proportion_confint
#import sys
#from jaratoolbox import behavioranalysis
#from jaratoolbox import settings 
from collections import Counter as cntr
#from scipy.stats import norm



subject = 'chad029'
paradigm = 'twochoice'
session = '20200317a'
behavFile = loadbehavior.path_to_behavior_data(subject,paradigm,session)
bdata = loadbehavior.BehaviorData(behavFile)
bdout = bdata['outcome']
cbdout = cntr(bdout)

'''
Summary Data
'''

#Fraction of correct choices
correct_choices = cbdout[1]
pr_correct = correct_choices / len(bdout)


#Fraction of stimuli that the animal missed
missed = cbdout[2]
pr_missed = missed / len(bdout)


#Fraction of responses taht are false alarms
false_alarms = cbdout[3]
pr_false_alarms = false_alarms / len(bdout)

'''
for the plot on the x it should be the stimulus intensity and on the y is the % trials correct
I know that Y is not working because I just have a count not an array. 
'''

plt.plot(bdout,  color='k', marker='x', lw=2)
plt.title('Chad029, 20200317a')
plt.xlabel('Trial #',fontsize=12) 
plt.ylabel('% Trials Correct (%)',fontsize=12)




plt.show()

'''
#another way of looking at the outcomes (changing what x is equal to)
n = len(bdout)
x = 1
def correct_occurence(bdout, n, x): 
    count = 0
    for i in range(n): 
        if x == bdout[i]: 
            count += 1
    return count
print(correct_occurence(bdout, n, x)
'''

'''
#plotting the data
# once I figure out how to make an array of correct responses then I can plot that below
plt.plot( )
plt.xlim()
plt.ylim()
plt.xlabel("Stimulus Intensity")
plt.ylabel("Proportion Correct")
'''
    
    
    