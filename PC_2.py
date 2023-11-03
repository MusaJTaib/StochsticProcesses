#Imports
import numpy as np
import matplotlib.pyplot as plt

#Initial Variable Initializations    
Output_2 = []
Output_6 = []
Output_100 = []
No_Bins_2 = 20
No_Bins_6 = 60
No_Bins_100 = 70
Total_Number = 100000


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
        
    plt.bar(y, hist_bars, width = increment, color='#444444')
   
#Main Code:

    
#Generating Distributions:
    
for r in range(Total_Number):
    #Sum of 2 variables
    No_Samples_2 = 2
    random_inputs_2 = np.random.uniform(10, 0, No_Samples_2)
    Sum_2 = sum(random_inputs_2)
    Output_2.append(Sum_2)


    #Sum of 6 variables
    No_Samples_6 = 6
    random_inputs_6 = np.random.uniform(10, 0, No_Samples_6)
    Sum_6 = sum(random_inputs_6)
    Output_6.append(Sum_6)
    

    #Sum of 100 variables
    No_Samples_100 = 100
    random_inputs_100 = np.random.uniform(10, 0, No_Samples_100)
    Sum_100 = sum(random_inputs_100)
    Output_100.append(Sum_100)
    
    
#Finding out the maximum and the minimum values in the dataset  
Max_2,Min_2 = Range(Output_2)
Max_6,Min_6 = Range(Output_6)
Max_100,Min_100 = Range(Output_100)

#Calculating Range of each distribution
Range_Axis_2 = Max_2 - Min_2 
Range_Axis_6 = Max_6 - Min_6 
Range_Axis_100 = Max_100 - Min_100

#Counting the number of values per bin for each distribution
Count_Bins_2 = np.array(CountFunction(Output_2, No_Bins_2,Range_Axis_2,Min_2))
Count_Bins_6 = np.array(CountFunction(Output_6, No_Bins_6,Range_Axis_6,Min_6))
Count_Bins_100 = np.array(CountFunction(Output_100, No_Bins_100,Range_Axis_100,Min_100))

#Bin Widths for each distribution
Bin_Width_2 = Range_Axis_2/No_Bins_2
Bin_Width_6 = Range_Axis_6/No_Bins_6
Bin_Width_100 = Range_Axis_100/No_Bins_100

#Normalizing BinCounts
Area_Histogram_2 = sum(Count_Bins_2*Bin_Width_2)
Area_Histogram_6 = sum(Count_Bins_6*Bin_Width_6)
Area_Histogram_100 = sum(Count_Bins_100*Bin_Width_100) 
  
Norm_Bins_2 = Count_Bins_2/Area_Histogram_2
Norm_Bins_6 = Count_Bins_6/Area_Histogram_6
Norm_Bins_100 = Count_Bins_100/Area_Histogram_100


#Plotting:

#Sum of 2 variables
Plot_Histogram(Norm_Bins_2, No_Bins_2,Range_Axis_2,Min_2)
plt.title('Sum of 2 variables (normalized)')
plt.xlabel('Value of X')
plt.ylabel('Probabilities')
plt.grid()
plt.show()

#Sum of 6 variables
Plot_Histogram(Norm_Bins_6, No_Bins_6,Range_Axis_6,Min_6)
plt.title('Sum of 6 variables (normalized)')
plt.xlabel('Value of X')
plt.ylabel('Probabilities')
plt.grid()
plt.show()

#Sum of 100 variables
Plot_Histogram(Norm_Bins_100, No_Bins_100,Range_Axis_100,Min_100)
plt.title('Sum of 100 variables (normalized)')
plt.xlabel('Value of X')
plt.ylabel('Probabilities')
plt.grid()
plt.show()










