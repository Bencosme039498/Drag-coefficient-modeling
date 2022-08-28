
"""
Created on Sun Jan  9 17:56:11 2022

@author: Juan BENCOSME
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from scipy.optimize import minimize 


data = pd.read_excel ("PYTHON IOPI.xlsx", sheet_name = "POROSITÉ")

def SumSquares0(c): 
    x = [data ["RE 10"], data ["RE 25"], data ["RE 100"], data ["RE 250"]]
    y = [data ["CD"], data ["CD2"], data ["CD3"], data ["CD4"]]
    Re = [10,25,100,250]
    i = 0
    fin = c[0]  + c[1]  * x[i] + (c[2]  + c[3]  * x[i]) / Re[i] + (c[4]  + c[5] * x[i]) / ((Re[i]) ** (1/2)) 
    residuals = fin - y[i]
    return np.sum(residuals ** 2)
 
def SumSquares1(c): 
    x = [data ["RE 10"], data ["RE 25"], data ["RE 100"], data ["RE 250"]]
    y = [data ["CD"], data ["CD2"], data ["CD3"], data ["CD4"]]
    Re = [10,25,100,250]
    i = 1
    fin = c[0]  + c[1]  * x[i] + (c[2]  + c[3]  * x[i]) / Re[i] + (c[4]  + c[5] * x[i]) / ((Re[i]) ** (1/2)) 
    residuals = fin - y[i]
    return np.sum(residuals ** 2)

def SumSquares2(c): 
    x = [data ["RE 10"], data ["RE 25"], data ["RE 100"], data ["RE 250"]]
    y = [data ["CD"], data ["CD2"], data ["CD3"], data ["CD4"]]
    Re = [10,25,100,250]
    i = 2
    fin = c[0]  + c[1]  * x[i] + (c[2]  + c[3]  * x[i]) / Re[i] + (c[4]  + c[5] * x[i]) / ((Re[i]) ** (1/2)) 
    residuals = fin - y[i]
    return np.sum(residuals ** 2)


def SumSquares3(c): 
    x = [data ["RE 10"], data ["RE 25"], data ["RE 100"], data ["RE 250"]]
    y = [data ["CD"], data ["CD2"], data ["CD3"], data ["CD4"]]
    Re = [10,25,100,250]
    i = 3
    fin = c[0]  + c[1]  * x[i] + (c[2]  + c[3]  * x[i]) / Re[i] + (c[4]  + c[5] * x[i]) / ((Re[i]) ** (1/2)) 
    residuals = fin - y[i]
    return np.sum(residuals ** 2)

plt.figure (figsize = (5,5), dpi = 1500) 
RE10 = plt.scatter (data ["RE 10"], data ["CD"]) 
RE25 =  plt.scatter (data ["RE 25"], data ["CD2"]) 
RE100 = plt.scatter (data ["RE 100"], data ["CD3"], marker = "v") 
RE250 = plt.scatter (data ["RE 250"], data ["CD4"], marker = "*")
plt.title ('Indépendance de CD sur porosité',  loc = 'center')
plt.xlabel("Porosité")
plt.ylabel("CD")
plt.grid()

plt.legend((RE10, RE25, RE100, RE250),
           ('RE 10', 'RE 25', 'RE 100', 'RE 250'),
           scatterpoints=1,
           loc='best',
           ncol=3,
           fontsize=8)

PaNotMi = [0, 0.68, 51.3, -18.4, 2.35, 1]

def SumSquaresNotMinimze(PaNotMi):

    x = [data ["RE 10"], data ["RE 25"], data ["RE 100"], data ["RE 250"]]
    Re = [10,25,100,250]
   

    for i in range(len(x)):
        f = lambda x, Re: PaNotMi[0] + PaNotMi[1] * x + (PaNotMi[2] + PaNotMi[3] * x) / Re + (PaNotMi[4] + PaNotMi[5] * x) / ((Re) ** (1/2)) 
        yfunct = f(x[i], Re[i])
        plt.plot (x[i], yfunct )

SumSquaresNotMinimze(PaNotMi)


plt.figure (figsize = (5,5), dpi = 1500) 
RE10 = plt.scatter (data ["RE 10"], data ["CD"]) 
RE25 =  plt.scatter (data ["RE 25"], data ["CD2"]) 
RE100 = plt.scatter (data ["RE 100"], data ["CD3"], marker = "v") 
RE250 = plt.scatter (data ["RE 250"], data ["CD4"], marker = "*")
plt.title ('Indépendance de CD sur porosité',  loc = 'center')
plt.xlabel("Porosité")
plt.ylabel("CD")
plt.grid()

plt.legend((RE10, RE25, RE100, RE250),
           ('RE 10', 'RE 25', 'RE 100', 'RE 250'),
           scatterpoints=1,
           loc='best',
           ncol=3,
           fontsize=8)

def SumSquaresMinimze(PaNotMi, i):

    x = [data ["RE 10"], data ["RE 25"], data ["RE 100"], data ["RE 250"]]
    Re = [10,25,100,250]
    
    f = lambda x, Re: PaNotMi[0] + PaNotMi[1] * x + (PaNotMi[2] + PaNotMi[3] * x) / Re + (PaNotMi[4] + PaNotMi[5] * x) / ((Re) ** (1/2)) 
    yfunct = f(x[i], Re[i])
    plt.plot (x[i], yfunct )


#Minimizando parametros y grafica 
BestParam0 = minimize(SumSquares0, [0, 0.68, 51.3, -18.4, 2.35, 1])
SumSquaresMinimze(BestParam0.x, 0)

BestParam1 = minimize(SumSquares1, [0, 0.68, 51.3, -18.4, 2.35, 1])
SumSquaresMinimze(BestParam1.x, 1)

BestParam2 = minimize(SumSquares2, [0, 0.68, 51.3, -18.4, 2.35, 1])
SumSquaresMinimze(BestParam2.x, 2)

BestParam3 = minimize(SumSquares3, [0, 0.68, 51.3, -18.4, 2.35, 1])
SumSquaresMinimze(BestParam3.x, 3)
