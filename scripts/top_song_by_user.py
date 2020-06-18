# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 23:42:29 2020

@author: eminy
"""

from write_file import write_file
from os import makedirs, path, remove
from sys import argv
import numpy as np
from collections import Counter

#Manage where the file will be write and get
#Directory is where the result will be stored
directory = "../users"

#data_directory is where data will be ridden
data_directory = "../data"

#Get the date of the command line to find the right file
date = argv[1]
log_name = "listen-"+date+".log"
print("Log file :", log_name)



def top_by_user():

    #Create the directory to store the results
    if not path.exists(directory):
        makedirs(directory)
    

    #If the file has alreadey been computed we remove it
    #We can't use the "w" in the write function because write information 
    #in the loop and we have to use "a"
    file_path = directory+"/"+"user_top50_" + date +".txt"
    if path.exists(file_path):
        remove(file_path)
    

    #range(30) is used to be sure to get all saved information by the log_reader script
    #this is because we do not know the exact number if we execute the two scripts in a row
    #to avoid useless round we make a breaking loop if the file number i does not exist
    for i in range(30):

        #Create the path of the file
        users_path = data_directory+"/usersStream_"+str(i)+"_"+date+".npy"
        

        #Get the extracted data from the saved dictionary
        if path.exists(users_path):
            user_tmp = np.load(users_path, allow_pickle=True)

            #Transform the ridden data to dictionary
            users_list = user_tmp.item()
        else:
            break

        #Sort the id of the users to get a sorted result file
        current = (s for s in sorted(users_list))

        #result where the content to write will be stored
        result = []
        

        #For each user its result is precessed
        for user in current:
            try:
                
                #users_list[user] contains all the listening of user
                #Counter() will count all the repetition of each song id
                #write_file function will return a string which will be stored in result
                #result is the variable which will written in the output file
                result.append(write_file(Counter(users_list[user]), user))
            except:
                print("Error with user number", user)

        #We make only few writes operations to reduce the execution time
        open(file_path, "a").write("\n".join(result))
        
   
    
    print("Top 50 songs by user has been written for the", log_name, "file")



top_by_user()
