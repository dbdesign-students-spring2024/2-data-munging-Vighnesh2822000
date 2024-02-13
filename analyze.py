# Place code below to do the analysis part of the assignment.
import csv
import os

fileos = os.path.join('data', 'clean_data.csv')
with open(fileos) as filecsv:
    readerobj = csv.DictReader(filecsv)
    year = []
    temp = []
    for row in readerobj:
        year += [row['Year']]
        temp += [row['J-D']]
    n = 0         # variable to hold the beginning index value
    m= 10         # variable to hold the final index value within a decade cycle
    avg = 0       # variable to hold the value of the average for a decade
    while m <= len(year):
        sum=0     # variable to add the temperature change each year
        for y in range(n,m):
            sum += float(temp[y])
        avg = round(sum/10,1)
        print(str('Between ' + year[n]) + " to " + str(year[m-1] + " the average temperature anamoly was " + str(avg)))  
       
        if len(year) - m < 10 and len(year) - m > 0:
            n = m
            m = len(year)
        else:
            n = m
            m += 10 
    
            