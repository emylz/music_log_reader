# Music log reader

## Table of contents
- [Introduction](#link1)
- [Solution used](#link2)
- [Setup](#link3)
- [Run](#link4)
   - [Get log](#link5)
   - [Run the scripts](#link6)

## Introduction <a id="link1">

This is a set of Python scripts to analyze logs. There is a set of logs files with streams in different countries by different users at a given date. These scripts enable to compute two files by day : one with the streams by country and one with the streams by user.

These scripts have been implemented with Python 3 and work with Linux.

## Solution used <a id="link2">

**The solution is composed by four scripts (without the log generator) :**

 - log_reader.py : this script reads the log as input. It will sort its information and will create numpy datafiles as output. The first one is countriesStream_YYYYMMDD.npy. This is a dictionary with all the streams sorted by country for the date YYYYMMDD. The other files are usersStream_i_YYYYMMDD.npy. 
 There are several slices of one big dictionary with the streams sorted by user for the date YYYYMMDD. The letter i is the number of the slice. 
  These slices are used to reduce the memory used by the script to write information by users. 
 
 - top_song_by_country.py :  this script computes the number of streams by country for each song in the log file. It takes as input the date of the day where we want the information. It produces as input a file with the information sorted by country.
 
 - top_song_by_user.py : this script computes the number of streams by user for each song in the log file. It takes as input the date of the day where we want the information. It produces as input a file with the information sorted by user.
 
 - write_file.py : this script is used to prepare the information before they will be written in the file. It is used as module in top_song_by_country.py and in top_song_by_user.py. The script has been designed to work with countries and users without needed information.



## Setup <a id="link3">

You have to get following packages installed on your machine. You can get them with the following Linux commands:

 - PyCountry
 ```bash
 pip3 install pycountry
 ```
This library is used to get the ISO code of the countries.
 
 - Numpy
```bash
 pip3 install numpy
 ``` 
 
 There are also packages like Collections, os, random itertools or sys which are built-in modules in Python3.

## Run <a id="link4">

### Get log <a id="link5">

The scripts run on Linux. Open a console and go to the directory "scripts" of the project. The project files and folders look like this : 
```bash
.
├── README
└── scripts
    └── log_generator.py
    └── log_reader.py
    └── top_song_by_country.py
    └── top_song_by_user.py
    └── write_file.py
```

If you have logs files, you can skip the following instruction and go to [Run the scripts](#link6).

If you do not have log file to read you can use the log_generator script to generate a log. You can choose the number of user, of song and of streams at the beginning of the log.

Use the following command :
```bash
python3 log_generator.py YYYYMMDD
```
where YYYYMMDD is the date of the streams.

###  Run the scripts <a id="link6"> 

You have logs files. You can start to analyze the logs.

**First you have to run log_reader.py with:**
```bash
python3 log_reader.py path/to/your/log/name_log.log
```
The script will read the log you passed as input with its path. After the processing, there will be a "data" directory that will be created in the main directory (the root of your project). The "data" directory contains dictionary with the extracted data from the logs.

**Then run top_song_by_country.py with :**
```bash
python3 top_song_by_country.py YYYYMMDD
```
With the date as input, the script will find in the "data" directory the associated dictionary and computes the last file country_top50_YYYYMMDD.txt with information by country. A new directory named "countries" will be created with the file.

**This is the same for top_song_by_user.py :**
```bash
python3 top_song_by_user.py YYYYMMDD
```
With the date as input, the script will find in the "data" directory the associated dictionaries and compute the last file user_top50_YYYYMMDD.txt with information by country. A new directory named "users" will be created with the file.


Now the project looks like :
```bash
.
├── README
├── scripts
    └── log_generator.py
    └── log_reader.py
    └── top_song_by_country.py
    └── top_song_by_user.py
    └── write_file.py
├── data
    └── countriesStream_YYYYMMDD.npy
    └── usersStream_0_YYYYMMDD.npy
    ...
    └── usersStream_n_YYYYMMDD.npy
├── countries
    └── country_top50_YYYYMMDD.txt
└── users
    └── user_top50_YYYYMMDD.txt
```

You can now find your files in the directories "users" and "countries".

