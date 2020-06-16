# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 23:42:16 2020

@author: eminy
"""

from write_file import write_file
from os import makedirs, path, remove
from sys import argv, getsizeof
import numpy as np
from collections import Counter
from pycountry import countries

#Manage where the file will be write and get
#Directory is where the result will be stored
directory = "../countries"

#data_directory is where data will be ridden
data_directory = "../data"

#Get the date of the command line to find the right file
date = argv[1]
log_name = "listen-"+date+".log"
print("Log file :", log_name)



#Create the path of the file
country_path = data_directory+"/countriesStream_"+date+".npy"


#Get the extracted data from the saved dictionary
tmp = np.load(country_path)


#Transform the ridden data to dictionary
countries_list = tmp.item()


def top_by_country():

    #Create the directory to store the results
    if not path.exists(directory):
        makedirs(directory)


    #path of the output result
    file_path = directory+"/"+"country_top50_" + date +".txt"


    #Sort the ISO code list of the countries to get a sorted result file
    #The list is sorted by ISO code and not by country
    current = (s for s in sorted(list(countries), key = lambda c : c.alpha_2))
    result = []
    

    #Browse the sorted list of ISO code to compute the result sorted by code
    for country in current:
        try:

            c = country.alpha_2
            
            #First check if there are streams from the current country
            #countries_list[c] contains all the listening of c
            #Counter() will count all the repetition of each song id
            #write_file function will return a string which will be stored in result
            #result is the variable which will written in the output file
            if(c in countries_list):
                result.append(write_file(Counter(countries_list[c]), c))
                
                
        except OSError as e:
            print(e)


    #We make only one write operation to reduce the execution time
    open(file_path, "w").write("\n".join(result))
    

    print("Top 50 songs by country has been written for the", log_name, "file")




top_by_country()
