# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:05:53 2021

@author: 14062
"""
#%% Import modules
import glob
import re

# %% Get list of files
files = glob.glob("test_files/*")

old_text = input('Enter text to replace in file: ') #Get the users string

new_text = input('Change text: ') #Get the users string

regex = re.compile(old_text) #Compile the string into a regex search

result = [f for f in files if re.search(regex, f)]  #Find all the files that match result

file_lst_trimmed = [re.sub(regex, new_text, file) for file in result]

print(file_lst_trimmed)



