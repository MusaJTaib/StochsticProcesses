#Imports:
    
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as ss
from scipy.integrate import quad
import scipy.stats

#Initial Variable Initializations:   
No_Bins = 10
No_Bins_Norm = 10
Total_Number = 100000



List_Distributions = [2,6,100] 
Number_Distributions = 3


''' 
For Testing Purpose: The code will give the expected results (95% of the time) 
by running both the cells of this code at once and Calculating results for all 
3 distributions at once.
 
However I run this code the following way:

List_Distributions = [100] #change this value to 2,6 and 100 one at a time
Number_Distributions = 1

Here I run the code cell wise and change values of List_Distributions one at a
time, which allows me to manually check each bin in every iterations
to see if it has less than 5 count and add bins.

'''

#Functions:
def Create_PDF_NormalDistribution(y,mean,SD):
    x = (y-mean)/SD
    pdf = ((1.0/np.sqrt(2*np.pi))*(np.exp(-((x)**2) / 2.0)))
    return pdf/SD

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
 
def ChiSquare(Obs_Bins,Exp_Bins,Distribution):
    c = np.sum((Obs_Bins-Exp_Bins)**2 / Exp_Bins)
    Freedom = len(Obs_Bins)-2
    confidence = 1-ss.gammainc(Freedom/2,c/2)
    print("Distribution sum of ",Distribution,"variables")
    print("Confidence Value = ",confidence)
    

##Main Code:

##Observed Distribution Generation
for i in range(Number_Distributions):
    Output = []    
    for r in range(Total_Number):
        No_Samples = List_Distributions[i]
        random_inputs = np.random.uniform(10, 0, No_Samples)
        Sum = sum(random_inputs)
        Output.append(Sum)
        
    #Calculating Range of the distribution    
    Max,Min = Range(Output)
    Range_Axis = Max - Min 
    
    #Counting the number of values per bin
    Obs_Bins = np.array(CountFunction(Output, No_Bins,Range_Axis,Min))
    
    
##Expected Distribution Generation:
    
    #BinWidths
    Bin_Width = Range_Axis/No_Bins
    
    #Calculating the Mean and the Standard Deviation of the Observed Distribution
    SD = np.std(Output)
    mean = np.mean(Output)
    
    #Calculating Upper and Lower Limits of Integration
    x_min = linspace(Min,(Max-Bin_Width),10)
    x_max = linspace((Min+Bin_Width),Max,10)
    Integral = [0]*10
    
    
    #Using integration to find the Area under the graph for each bin interval
    for i in range(0, 10): 
        Integral[i], _ = quad(Create_PDF_NormalDistribution, x_min[i], x_max[i], args=(mean,SD))
    
    #Calculating Expected Bin Counts Using Integral
    Exp_Bins = [100000]*10
    Exp_Bins = np.array(Exp_Bins)
    Exp_Bins = Exp_Bins*Integral
    Exp_Bins = np.round(Exp_Bins)
    
#%%    
'''Chi_Square_Test - Only run this cell seperately from the rest of the code 
   if you want to manually add bins''' 
    
    #Summing Bins Manually to make sure bin count for no bin is less than 5       
    Obs_Bins = np.array([ Obs_Bins[0]+Obs_Bins[1], Obs_Bins[2], Obs_Bins[3], Obs_Bins[4], 
                          Obs_Bins[5], Obs_Bins[6], Obs_Bins[7], Obs_Bins[8]+ Obs_Bins[9]])
    
    Exp_Bins = np.array([ Exp_Bins[0]+Exp_Bins[1], Exp_Bins[2], Exp_Bins[3], Exp_Bins[4], 
                          Exp_Bins[5], Exp_Bins[6], Exp_Bins[7], Exp_Bins[8]+ Exp_Bins[9]])
  

    ChiSquare(Obs_Bins, Exp_Bins,No_Samples)
    
   
