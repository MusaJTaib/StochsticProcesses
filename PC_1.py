#Imports

import numpy as np
import matplotlib.pyplot as plt


#Functions:    

def Range(x):
    return max(x),min(x)

def CountFunction(Input,Bins,Range_Axis,Min):
    Increment_PerBin = Range_Axis/Bins
    Output_Bins = [0]*Bins
    for L in range (0,Bins):
        Count = L
        for Number in Input:
            if ((Number>=Min+L*Increment_PerBin) and (Number<Min+((L+1)*Increment_PerBin))):
                Output_Bins[Count] = Output_Bins[Count]+1
    return Output_Bins

def Plot_Histogram(Bins,No_Bins,Range_Axis,Min):
    hist_bars = Bins
    increment = Range_Axis/No_Bins
    b = Min + increment/2
    y = []
    
    for x in range(No_Bins):
        y.append(b)
        b = b+increment
        
    plt.bar(y, hist_bars, width = increment, color='#444444',label = "Numerical")
    

##MainCode
#Numerical PDF

Total_Number = 100000 
No_Bins = 25
Output = np.random.uniform(-3, 3, Total_Number)


#Finding out the maximum and the minimum values in the dataset  
Max,Min = Range(Output)

#Calculating Range of each Graph
Range_Axis = Max - Min 


#Counting the number of values per bin
Count_Bins = np.array(CountFunction(Output, No_Bins,Range_Axis,Min))



#Bin Widths
Bin_Width = np.array(Range_Axis/No_Bins)


#Normalizing BinCounts
Area_Histogram = sum(Count_Bins*Bin_Width)  
Norm_Bins = Count_Bins/Area_Histogram


#Theoratical PDF
x_values = np.linspace(-3,3,100000)
pdf = 1/Range_Axis*(x_values/x_values)


#Plotting both Theoratical and Numerical PDFs
plt.plot(x_values,pdf, '-r', label='Theoratical')
Plot_Histogram(Norm_Bins, No_Bins,Range_Axis,Min)
plt.title('Graph Normalized')
plt.xlabel('Value of X')
plt.ylabel('Probabilities')
plt.legend()
plt.grid()
plt.show()












