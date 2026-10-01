import numpy as np
import matplotlib.pyplot as plt
import copy

class Household:
    def __init__(self, income):
        self.income = income
        self.co2 = co2(income)

 


def randomincome(mean=4800, gini = 0.45):
    inc = np.random.lognormal(np.log(mean), gini)
    return inc

def co2(income):
    base_co2 = 3
    slope_co2 = 2.4
    
    log_income = np.log(income)
    co2 = base_co2 + slope_co2 * log_income
    

    return co2
    
def plothouseholds(hh):
    incs=[]
    co2s=[]
    for h in hh:
        incs.append(h.income)
        co2s.append(h.co2)
    incs=sorted(incs)
    co2s = sorted(co2s)
    plt.figure()
    plt.plot(incs, color="forestgreen")
    plt.figure()
    plt.plot(co2s,color="gray")
    plt.show()

def compareplot(a,b):
    incsa=[]
    incsb=[]
    co2sa=[]
    co2sb=[]

    for h in a:
        incsa.append(h.income)
        co2sa.append(h.co2)
    for h in b:
        incsb.append(h.income)
        co2sb.append(h.co2)

    incsa=sorted(incsa)
    incsb=sorted(incsb)
    co2sa=sorted(co2sa)
    co2sb=sorted(co2sb)

    plt.figure()

    plt.plot(incsa,color="lime")
    plt.plot(incsb,color="forestgreen")

    plt.figure()
    
    plt.plot(co2sa,color="gray")
    plt.plot(co2sb,color="black")
    

    print("poorest household:",incsa[0],"->",incsb[0])
    print("overall emissions:",sum(co2sa),"->",sum(co2sb))

    plt.show()

def updateco2(hh):
    for h in hh:
        h.co2 = co2(h.income)
     




def co2_tax(hh, co2cost=500):
   
   
    taxes = []
    for h in hh:
        tax = co2cost * h.co2
        taxes.append(tax)

   
    transfer =  sum(taxes)/ len(hh)
   

    for it in range(len(hh)):
        hh[it].income = hh[it].income - taxes[it] + transfer

    return hh

def main():
    households = []
    for it in range(10000):
        households.append(Household(randomincome()))
    households_old=copy.deepcopy(households)

    households2=co2_tax(households)

    updateco2(households2)
    compareplot(households_old,households2)

main()

