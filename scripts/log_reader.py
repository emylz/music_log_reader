# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:35:18 2020

@author: eminy
"""

from sys import argv
import numpy as np
import os
from itertools import islice

#Dictionary where all information by country will be stored
#Each key of the dictionary is a country ISO code and 
#each value is a list with all the song id listened in the country
countries_list = {}

#Dictionary where all information by user will be stored
#This is the same that for countries list except
#that users id replace countries ISO code
user_list = {}


#Get the path of the log file from the execution command line
path = argv[1]
print("Log file to read:", path)


#Log name format :
#path/to/file/listen-YYYYMMDD.log
#First get the last element after spliting by "-" : YYYYMMDD.log
#Then get the first element after spliting by "." : YYYYMMDD
date = path.split("-")[-1]
date = date.split(".")[0]

def stream_by_country(song_id, country):

    #If the country has already been read
    #the song id is add to its list
    if(country in countries_list):
        countries_list[country].append(song_id)
    else:
        #The country is read for the first time
        #We add a key with the country ISO code 
        #And a list as value containing the song id
        countries_list[country] = [song_id]       



def stream_by_user(song_id, user_id):

    #If the user has already been read
    #the song id is add to its list
    if(user_id in user_list):
        user_list[user_id].append(song_id)
    else:
        #The user is read for the first time
        #We add a key with the user id 
        #And a list as value containing the song id
        user_list[user_id] = [song_id]



def read_log_file():

    #We read the log file
    f = open(path, "r")
    print("Read log data")

    #Create a generator with all lines of the log
    #The usage of generator allow to use less memory 
    #and is faster
    #It avoids memory issues too
    gen = (line for line in f)

    #return the generator
    return gen



#This funtion allow to create several chunks from a dictionary
#data is the data to split into chunks
#size is the size of each chunks
def chunks (data, size):

    #The data parameter is transformed as an iterable object
    #The data is sorted to have the key in sorted order
    #It will be easier to get the data in sorted order when scripts will read it
    it = iter(sorted(data))

    #The loop will run until the end of the data
    #with size as step to split data
    for i in range(0, len(data), size):

        #yield each key/value pair friom the slice returned by islice
        #it is the iterable object to split
        #size is the size of each slice
        yield {k:data[k] for k in islice(it, size)}



def stream():
    
    #This is the directory where the data will be stored after processing
    #If this directory does not exist it is created
    directory = "../data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    #This gets all data the file with the function read_log_file()
    #listening_list is a generator
    listening_list = read_log_file()
    
    
    print("Sort data")
    #For each line gets from the file
    #we get the differents information
    #it make only one loop for users and countries
    #to reduce the execution time
    for cat in listening_list:
        try:
            
            #Split the line according to the log format
            tmp = cat.split(" | ")


            #Extract the information
            #song_id and user_id are converted in int
            #because this is more memory efficiant than in string
            #rstrip() is used in case of there is a malformated log with more spaces
            song_id = int(tmp[0].rstrip())
            user_id = int(tmp[1].rstrip())


            #Remove the line break ("\n") with rstrip()
            country = tmp[2].rstrip()

            #Check if the log has no problems
            if(len(tmp) == 3 and len(country) == 2):

                #Sort information for the countries
                stream_by_country(song_id, country)

                #Sort information for the user
                stream_by_user(song_id, user_id)

            else:
            	print("Corrupted log found")

        except :
            #Print the error in case of error like corrupted log
            print("Corrupted log found")
    
    print("Save read data")



    print("Save data about the countries")

    #Save the dictionary with informations of the countries
    #The dictionary will be save in the directory defined
    #at the begining of the function
    #the date is added to make difference between dictionaries after saving
    country_path = directory+"/countriesStream_"+date+".npy"
    np.save(country_path, countries_list)

    #The the dictionary become empty
    countries_list.clear()


    
    print("Save data about the users")
    i = 0

    #This is the size in number of keys of each dictionary which will be created
    size = 2000000

    #Split the dictionary with the chunks funtion
    for item in chunks(user_list, size):

        #item is a slice of the original dicionary
        tmp = item

        #item is saved and the variable i is used to make difference
        #between all slices of the dictionary
        #the date is added to make difference between dictionaries after saving
        user_path = directory+"/usersStream_"+str(i)+"_"+date+".npy"
        np.save(user_path, tmp)

        i+=1

    #The the dictionary become empty
    user_list.clear()


    print("Log has been read")
        

       
stream()  
