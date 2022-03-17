#importing libraries
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import pylab as P
import csv 

#opening all files in this file
exec(open('Extrema.py').read())
exec(open('monotonic.py').read())
exec(open('splineFit.py').read())
exec(open('plot.py').read())


#opening the excel file 
with open ("data.csv") as csvfile:
    readCSV=csv.reader(csvfile, delimiter=',')

    # creating lists seperately for x and y values
    timeSeries=[]
    for row in readCSV:
        timeSeries.append(float(row[0]))

# number of data points
print("Number of data points found: ", len(timeSeries))

current_set = timeSeries
IMFs= []
IMFs.append(timeSeries)

while True:
    series_length=len(current_set)
    
    Minima_indices=get_minimaIndices(current_set)
    Minimas=get_minima(current_set)
    Maxima_indices=get_maximaIndices(current_set)
    Maximas=get_maxima(current_set)
    
    print(Maximas)
    print(Maxima_indices)
    
    if len(Minimas) >1 and len(Maximas) >1:

        if len(Minimas) <=3:
            
            kis=1
        else:
            kis=3
    
        splfit_max= splinefit(Maximas, Maxima_indices, series_length, kis) #upper evelop
        splfit_min= splinefit(Minimas, Minima_indices, series_length, kis) #lower evelop
        print(splfit_max)
    
        Minima_indices=[]
        Minimas=[]
        Maxima_indices=[]
        Maximas=[]
        
        loopx=0
        mean_of_ExtremaEnvelops=[]
        while loopx <= len(splfit_min)-1:
            mean_of_ExtremaEnvelops.append( (splfit_min[loopx]+splfit_max[loopx])/2 )
            loopx+=1
            
        loopx=0
        Remainder=[]
        while loopx <= len(current_set) -1:
            Remainder.append(current_set[loopx] - mean_of_ExtremaEnvelops[loopx])
            loopx+=1
        
        
        
        
        Minima_IndicesIMF=get_minimaIndices(Remainder)
        MinimaIMF=get_minima(Remainder)
        Maxima_IndicesIMF=get_maximaIndices(Remainder)
        MaximasIMF=get_maxima(Remainder)

        number_of_max_min_diff=abs(len(Maxima_IndicesIMF)-len(Minima_IndicesIMF))

        if monotonic(Remainder) == False and (number_of_max_min_diff <=1):
            IMFs.append(Remainder)
            #print(IMFs)

            new_set=[]
            loopy=0
            while loopy <= len(current_set) -1:
                new_set.append(current_set[loopy]-Remainder[loopy])
                loopy+=1
            #print(new_set)
            current_set = new_set
    
        else:
            break

    else:
        IMFs.append(current_set)
        break
print(IMFs)
     
loopx=0
up_truncate=0
down_truncate=0
while loopx<=len(IMFs)-1:          
    IMFs[loopx]=IMFs[loopx][up_truncate:series_length-down_truncate]
    loopx+=1





plt.figure(1)
no_of_IMFs=len(IMFs)
x_values=range(1, len(IMFs[0])+1)
   
loopx=0
while loopx<=no_of_IMFs-1:
    plt.subplot(no_of_IMFs,1,loopx+1) # row 2, col 1, num 1(top)
    plt.plot(x_values,IMFs[loopx],'r--') 
    plt.xlabel('Time stamp')
    plt.ylabel('IMF'+str(loopx+1))
    plt.show(block=False)
    loopx+=1
    
    
    
    





























 