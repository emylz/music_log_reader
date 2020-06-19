# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:40:05 2020

@author: eminy
"""


from random import randrange

#Library with all countries information
from pycountry import countries
from sys import argv

#The list of all countries in the world
list_countries = list(countries)

#The estimate number of user
user_count = 10000000

#The estimate number of available songs
song_count = 30000000

#The number of listening
listening_count = 30000000

#Date of the listening of the logs
#Get from the execution command line
date = argv[1]


def write_log_file():

	#File name of the output log
    file_name = "../listen-"+date+".log"

    #tmp is a string where all the log will be stored
    tmp = ''


    for i in range(listening_count):

    	#Get a random country
    	#len(list_countries) allow to have a random int smaller 
    	#than the size of the list
        rand_country = randrange(len(list_countries))

        #Get the ISO code of the selected country
        country = list_countries[rand_country].alpha_2

        #Get a random user id smaller than the number of user
        user_id = randrange(user_count)

        #Get a random song id smaller than the number of user
        song_id = randrange(song_count)

        #The format of the log
        log = str(song_id)+" | " + str(user_id)+" | "+country + "\n"

        #Add the log to the output variable
        tmp += log

    #We make only one write operation to reduce the execution time
    open(file_name, "a").write(tmp)
        

write_log_file()
        



