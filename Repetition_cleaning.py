
#!/bin/bash/env python
# PREPROCESSING STEPS:
# 1) Find and Replace (Delete) all spaces in datasets .csv
# 2) delete all empty columns
##########
# This script deletes rows that are not of interest 



#Import modules
import pandas as pd


# Sepcify csv file name to import
DATA = '8100_ICUY_20160216_readable.csv'

#Specify output name
OUTPUT = open('Edited_8100_ICUY_20160216_readable.csv', 'w+')


# Read data file as csv
DATACSV = pd.read_csv(DATA)


# Make it a DataFrame
df_DATACSV = pd.DataFrame(DATACSV)

#Drop observations that contain a string: Basically create a new DataFrame
#That doesn't contain raws wich had the value 'V1REP'

df_DATACSV[df_DATACSV.Visit != 'V1REP'] #Visit is the column (as python method), V1REP is the value

# Specify file path to save DataFrame as csv

df_DATACSV.to_csv(OUTPUT)




