"""
Created on Wed May 27 14:30:00 2022

@author: Angelos Martidis - mai22042
"""

import numpy as np
import random as random
import copy

#import sys
#np.set_printoptions(threshold=sys.maxsize)

tableA=[] #table for every t
tableB=[] #temporary table for saving values
tableC=[] #weigh factor table
posprob=[] #probability table
windprob=[] #probability table
savedpos=[]
savedwind=[]




def make_init(tableA):                      #initial condition creation
    tableA=np.random.randint(1,4,int(10e2)) #number of samples generated for the problem can be changed here
    for i in range(len(tableA)):
#       x=random.random()
#       if x < 0.5 :                        #if i want to have random sign for the initial condition
#       for the asked initial condition Wind is E (-)
        tableA[i]=tableA[i]*(-1)
    print('''
Explanation:
	
1 is for Position Left L.
2 is for Position Centre C.
3 is for Position Right R.
        
(-) Negative Values are for East Wind E.
(+) Possitive Values are for West Wind W.

TableA contains the values after every transition for (time)t(i).
TableB contains the next values (for t(i)+1) of TableA.
TableC contains the Weight Factors of TableA for (time)t(i).
Tableposprob contains Position's Probabilities : [ L , C , R ] asked for (time)t(i).
Tablewindprob contains Wind's Probabilities : [ E , W ]  asked for (time)t(i).

On every iteration equality of TableA and TableC is checked.
Therefore it is normal to return False at last iteration, as 
there are not any observations for t=4 according to the problem encountered.       
''')
    return tableA

def wind(tableA):
    for i in range(len(tableA)):
        x=random.random()
        if x>= 0.7 : 
            if tableA[i] < 0 :              #if Wind E then do this
                tableA[i]=tableA[i]*(-1)
        if x<= 0.3 :
            if tableA[i] > 0 :              #if Wind W then do this
                tableA[i]=tableA[i]*(-1)
    return tableA

def position(tableA):
    for i in range(len(tableA)):            #position values dont change for LE,RW
        x=random.random()
        if tableA[i] == -2 and x <= 0.5 :   #for CE
            tableA[i] = -3
        if tableA[i] == -1 and x <= 0.5 :   #for RE
            tableA[i] = -2
        if tableA[i] == 2 and x >= 0.5 :    #for CW
            tableA[i] = 3
        if tableA[i] == 1 and x >= 0.5 :    #for LW
            tableA[i] = 2 
    return tableA

def weight_factor(tableC):
    for i in range(len(tableA)):
        if abs(tableA[i])==1 or abs(tableA[i])==3: 
            tableC.append(0.2)
        if abs(tableA[i])==2:
            tableC.append(0.4)
    return tableC

def sampling(tableB,tableA):
    csum = sum(tableC)
    for i in range(len(tableA)):
        x = random.random()*csum
        tempsum=0
        y=False
        for k in range(len(tableC)):
            tempsum += tableC[k]
            if tempsum > x and y==False :
                tableB.append(tableA[k])
                y=True
    return tableA,tableB

def presentProbP(tableA) :                   #Calculation of present time position probability
    posprob.clear()
    x = np.absolute(tableA)                  #if i want to save it on a list
    for i in range(1,4):
        tempcount = np.count_nonzero(x == i)
        # find posprob upto 2 decimal places
        posprob.append(tempcount / len(tableA))
    return posprob

def presentProbW(tableA) :                   #Calculation of present time wind probability
    windprob.clear()
    #1st way to count negative and positive values wuth lambda expression
    pos_count = len(list(filter(lambda x: x > 0, tableA)))
    neg_count = len(list(filter(lambda x: x < 0, tableA)))
    
    #2nd way to count possitive and negative values with itteration
    #pos_count, neg_count = 0, 0  
    # iterating each number in list
    #for num in tableA:
    #      
    #    # checking condition
    #    if num > 0:
    #        pos_count += 1
    #  
    #    else:
    #        neg_count += 1
    
    windprob.append(pos_count / len(tableA))
    windprob.append(neg_count / len(tableA))
    
    #3rd way to count possitive and negative values w/out NUMPY            
    #windprob.append((tableA<0).sum()/len(tableA))
    #windprob.append((tableA>0).sum()/len(tableA))
    
    return windprob

def asked_data(t,posprob,windprob,savedpos,savedwind):
    if t>=2 and t<=4:
        savedpos.append(copy.deepcopy(posprob))
        savedwind.append(copy.deepcopy(windprob))
    return savedpos,savedwind

def print_list(l,size):
    for x in l: 
        print(x[2])


t=0
tableA=make_init(tableA)
#print('TableA has these values for t=0 : \n',tableA)
while t<4:
    t+=1
    print("\nIteration for (time) t=%.i : \n" %(t))
    wind(tableA)
    #print("Performing Wind's transition model for (time) t=%.i : \n " %(t),tableA)
    position(tableA)
    #print("Performing Position's transition model for (time) t=%.i : \n " %(t),tableA)
    weight_factor(tableC)
    #print("TableC of Weight Factors for (time) t=%.i : \n " %(t),tableC)
    ##print("TableA has these values for (time) t=%.i : \n " %(t),tableA)
    if t!=4:
        sampling(tableB,tableA)
        tableA=np.copy(tableB)
        print("Sampling....")
        print("Check sizes of both tableA and B: ",len(tableA)==len(tableB))
    print("Values from tableB(after Sampling) replaced on tableA: ",np.array_equal(tableA,tableB))
    presentProbP(tableA)
    presentProbW(tableA)
    asked_data(t,posprob,windprob,savedpos,savedwind)
    #print("\n\n PROBABILITY L :",probab[0])
    #print("\n\n PROBABILITY C :",probab[1])
    #print("\n\n PROBABILITY R :",probab[2])
    #print("TableA has these values for t=%.i : \n " %(t),tableA)
    print("\nPosition's Probabilities : [ L , C , R ] = %a" %(posprob))
    print("\nWind's Probabilities : [ E , W ] = %a" %(windprob))
    tableC.clear()
    tableB.clear()
print("The results are :"
"\nP(X2) :",savedpos[0],
"\nP(X3) :",savedpos[1],
"\nP(X4) :",savedpos[2],
"\nP(A2) :",savedwind[0],
"\nP(A3) :",savedwind[1],
"\nP(A4) :",savedwind[2])

print("\nThe results are :")
t=2
for j in range(len(savedpos)):
    print("\nP(X%.i):" %(t))
    for i in range(len(savedpos)):
        if i==0:
            print('L :',savedpos[j][i])
            #print(savedpos[j][i])
        if i==1:
            print('C :',savedpos[j][i])
            #print(savedpos[j][i])
        if i==2:
            print('R :',savedpos[j][i])
            #print(savedpos[j][i])
    t=t+1
t=2
for j in range(len(savedwind)):
    print("\nP(A%.i):" %(t))
    for i in range(len(savedwind)):
        if i==0:
            print('E :',savedwind[j][i])
            #print(savedwind[j][i])
        if i==1:
            print('W :',savedwind[j][i])
            #print(savedwind[j][i])
    t=t+1
