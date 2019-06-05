# -*- coding: utf-8 -*-
"""
Created on Sun May 19 08:21:30 2019

@author: hp
"""

import numpy as np
import csv

movie_names = np.loadtxt('movies1_name.txt', dtype='str', usecols=None, delimiter='\n') 
print(movie_names)
    
with open('recom_movies.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows([movie_names])
