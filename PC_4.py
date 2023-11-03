#Imports
import numpy as np

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
    
