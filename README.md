# Music log reader

## Introduction

This is a set of Python scripts to analyze logs. There is a set of logs files with streams in differents countries by differents users at a given date. Theses scripts allow to compute two file by day : one with the streams by country and one with the streams by user.

Theses scripts have been implemented with Python 3 and work with Linux.

## Solution used

The solution is composed by four scripts (without the log generator) : 

 - log_reader.py : this script reads the log as input. It will sort its information and will create numpy datafiles as output. The first one is countriesStream_YYYYMMDD.npy. This is a dictionary all the streams sorted by country for the date YYYYMMDD. The other files are usersStream_i_YYYYMMDD.npy. Theses are several slices of one big dictionary with the streams sorted by user for the date YYYYMMDD. i is the number of the slice. 
  Theses slices are used to reduce the memory used by the script to write information by users. 
 
 - top_song_by_country.py :  this script compute the number of streams by country for each song in the log file. It takes as input the date of the day where we want the information. It produces as in put a file with the information sorted by country.
 
 - top_song_by_user.py : this script compute the number of streams by user for each song in the log file. It takes as input the date of the day where we want the information. It produces as in put a file with the information sorted by user.
 
 - write_file.py : this script is used to prepare the information before they will be written in the file. It is used as module in top_song_by_country.py and in top_song_by_user.py. The script has been designed to work with countries and users without needed information.



## Setup

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

## Run

### Get log

The scripts run on Linux. Open a konsole and go to the directory scripts of the project. The project files and folders look like this : 
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

If you have logs files, you can skip the following instruction and go to [Run the scripts](#link)

If you do not have log file to read you can use the log_generator script to generate a log. You can choose the number of user, of song and of streams at the beginning of the log.

Use the following command :
```bash
python3 log_generator.py YYYYMMDD
```
where YYYYMMDD is the date of the streams.

### <a id="link">Run the scripts

You have logs files. You can start to analyze the logs.

First you have to run log_read.py with:
```bash
python3 log_generator.py path/to/your/log/name_log.log
```
The script will read the log you passed as input. After the processing, there will be a data directory that will be created in the main directory (the root of your project). The data directory contain dictionary with the extracted data from the logs.

Then run top_song_by_country.py with:
First you have to run log_read.py with:
```bash
python3 top_song_by_country.py YYYYMMDD
```
With the date as input, the script will find in data the associated dictionary and compute the last file country_top50_YYYYMMDD.txt with information by country. A new directory countries will be created with the file.

This is the same for top_song_by_user.py:
```bash
python3 top_song_by_user.py YYYYMMDD
```
With the date as input, the script will find in data the associated dictionaries and compute the last file user_top50_YYYYMMDD.txt with information by country. A new directory users will be created with the file.




