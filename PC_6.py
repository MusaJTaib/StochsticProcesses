import numpy as np
TSPoints = 200


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
    Ensemble[w] = realization #Equating the successive realizations to rows of the Ensemble
    w = w + 1
    

##Question 6 Tasks Start


##Numerical Auto-Correlation

'''We know that for pdf of a stochasitc process we looks at the x (vertical values) 
   and not t (horizontal values)'''


#Question 6 Specific Initializations
Auto_Correlation_Num = [0.0]*200
Auto_Correlation_Num = np.array(Auto_Correlation_Num)
PDF_Values = [0.0]*10000
PDF_ValuesT1 = np.full(10000, 0.0) #Values at T1

#I will keep T1 fixed at timeshift of 0 at all times 
for X in range(10000):
        #Equating all Values at timeshift of 0 to PDF_Values1 Variable
        PDF_ValuesT1[X] = Ensemble[X][0] 
        

#T2 will sweep from 0 to 200
for Y in range (200):
    PDF_ValuesT2 = np.full(10000, 0.0) #Values at T2
    for X in range(10000):
        PDF_ValuesT2[X] = Ensemble[X][Y] # Row x Coloumn
    PDF_ValuesT2 = PDF_ValuesT1*PDF_ValuesT2 #Product of T1*T2
    PDF_ValuesT2 = sum(PDF_ValuesT2) 
    Average = PDF_ValuesT2/10000
    Auto_Correlation_Num[Y] = Average
    

##Theoratical Auto Correlation

#Plotting the auto-correlation equation:
y1 = cos(Theeta) # Theeta = w(t2-t1)
y2 = 0.5
Auto_Correlation_Theo = y2*y1 # Auto Correlation = (1/2)Cos(w(t2-t1))


##Plotting

#Seperate Plots
plt.plot(Theeta,Auto_Correlation_Num,'b', label = "Numerical Auto-Correlation")
plt.title('Graph of Numerical Auto-Correlation')
plt.xlabel('Value of T2 - T1')
plt.ylabel('Value of Auto-Correlation')
plt.legend(loc='upper left')
plt.ylim(-2, 2)
plt.grid()
plt.show()

plt.plot(Theeta,Auto_Correlation_Theo, 'r', label = "Theoratical Auto-Correlation")
plt.title('Graph of Theoratical Auto correlation')
plt.xlabel('Value of T2 - T1')
plt.ylabel('Value of Auto-Correlation')
plt.legend(loc='upper left')
plt.ylim(-2, 2)
plt.grid()
plt.show()


#Combined Plot
'''Notice that the purple colour of the output graph is because the sum of red + blue
   graphs results in a purple graph'''
plt.plot(Theeta,Auto_Correlation_Theo, 'r', label = "Theoratical Auto-Correlation")
plt.plot(Theeta,Auto_Correlation_Num,'b', label = "Numerical Auto-Correlation")
plt.title('Graph of Numerical Auto-Correlation vs Theoratical Auto correlation')
plt.xlabel('Value of T2 - T1')
plt.ylabel('Value of Auto-Correlation')
plt.legend(loc='upper left')
plt.ylim(-2, 2)
plt.grid()
plt.show()