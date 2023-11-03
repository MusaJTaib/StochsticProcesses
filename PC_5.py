#Imports
import numpy as np

##Ensemble Generation Code from Question 4

#Function = Sin(Theeta+Phi)

#Initial Variable Initializations    
TSPoints = 10*20
Ensemble = [0]*10000

#Generatiing Theeta Values
Theeta = linspace(0,2*(np.pi)*10,200)    

#Generating Values of Phi for each Realization of the Ensemble
Phi = np.random.uniform(0, 2*(np.pi), 10000)

#Generating Ensemble
w = 0
for x in Phi:
    realization = [0]*TSPoints #Generating a zero padded list for every realization
    z = 0
    for y in Theeta:
        realization[z] = sin(y+x)
        z = z +1
    Ensemble[w] = realization #Equating successive realizations to rows of the Ensemble
    w = w + 1
    
    
    
##Question 5 Task Start:
#Variables Specifically required for Q5
No_Bins = 100
Total_Number = 10000


#Functions:

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

   
'''We know that for pdf of a stochasitc process we looks at the x (vertical values) 
   and not t (horizontal values)'''


##Numerical PDF
#Taking the first value from each of the 10,000 realizations
PDF_Values = [0]*10000
for X in range(10000):
    PDF_Values[X] = Ensemble[X][0] # Row x Coloumn
    
#Finding out the maximum and the minimum values in the dataset  
Max,Min = Range(PDF_Values)

#Calculating Range of each Graph
Range_Axis = Max - Min 

#Counting the number of values per bin
Count_Bins = np.array(CountFunction(PDF_Values, No_Bins,Range_Axis,Min))

#Bin Widths
Bin_Width = np.array(Range_Axis/No_Bins)

#Normalizing BinCounts
Area_Histogram = sum(Count_Bins*Bin_Width)  
Norm_Bins = Count_Bins/Area_Histogram

##Theoratical PDF
x_values = np.linspace(-1,1,10000)

y1 = sqrt(1-x_values**2)
y2 = (np.pi)*(y1)
pdf = 1/y2

#Plotting both Theoratical and Numerical PDFs
plt.plot(x_values,pdf, '-r', label='Theoratical')
Plot_Histogram(Norm_Bins, No_Bins,Range_Axis,Min)
plt.title('Graph Normalized')
plt.xlabel('Value of X')
plt.ylabel('Probabilities')
plt.legend()
plt.grid()
plt.show()

