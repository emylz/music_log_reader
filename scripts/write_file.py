# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 00:24:56 2020

@author: eminy
"""
def write_file(result, id):

    #Get the user id/country code
    tmp = str(id)
    
    #Format of the output
    tmp += " | "

    #Number of n first song id to write
    top = 50

    i = 0
 
    result_size = len(result)
    if(result_size < top):

        #If there is less listened music for this user/country than 50
        #we take only its n first values 
        #to avoid an out of range error
        top = result_size


    #We extract the n first id of the user/country
    #most_commont return the n most common item (n is the parameter)
    for r in result.most_common(top):

        #Get the song id
        #Result is a list of tuple
        #The id is at index 0
        idSong = str(r[0])
        tmp += idSong
        
        #Format of the output
        tmp += ":"
        
        #Get the number of listening from the current id song
        #The number of listening is at index 1
        number_of_listening = str(r[1])
        tmp += number_of_listening

        #Format of the output
        if(i != top-1):
            tmp += ","
        i+=1
    
    #tmp is string where we will join all information of the current user/country
    return tmp