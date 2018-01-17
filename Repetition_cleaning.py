
#!/bin/bash/env python

##########
# This script 
# removes spaces from column names
# removes empty columns
# deletes rows that are not of interest
##########


#Import modules
import pandas as pd


# Sepcify csv file name to import
DATA = '8100_STAI_20160216_readable.csv'

#Specify output name
OUTPUT = open('11Edited_8100_STAI_20160216_readable.csv', 'w+')


# Read data file as csv
#Doesn't import first row, needed for NKI, otherwise set skiprows=False
#2nd row (or first remaining) row as column headers
DATACSV = pd.read_csv(DATA, skiprows=0, header=1)


# Make it a DataFrame
df_DATACSV = pd.DataFrame(DATACSV)

# Remove spaces from column names
df_DATACSV.columns = df_DATACSV.columns.str.replace('\s+', '') 


#Remove empty columns
df_DATACSV = df_DATACSV.dropna(how='all', axis=1)  


#Drop observations that contain a string: Basically create a new DataFrame
#That doesn't contain raws wich had the value 'V1REP'

df_DATACSV = df_DATACSV[df_DATACSV.Visit != 'V1REP'] #Visit is the column (as python method), V1REP is the value

# Specify file path to save DataFrame as csv

df_DATACSV.to_csv(OUTPUT)







