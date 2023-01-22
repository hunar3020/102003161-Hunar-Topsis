import numpy as np
import pandas as pd 
import math 
import sys 
from tabulate import tabulate
from os import path 


def topsis(data,Weights,effect,resultName):
    df = pd.read_csv(data)
    df.dropna(inplace = True)
    dfNumeric = df.iloc[0:,1:].values
    matrix = pd.Dataframe(dfNumeric)
    sumofSquares = []
    for col in range(0,len(matrix.columns)):
        x= matrix.iloc[0:,[col]].values
        for i in x:
            sum=0
            sum += (i*i)
        sumofSquares.append(math.sqrt(sum))
        j=0
    while(j<len(matrix.columns)):
        for i in range(0,len(matrix)):
            matrix[j][i] /= sumofSquares[j]
        j+=1
                
        k=0
    while(k<len(matrix.columns)):
        for i in range(0,len(matrix)):
            matrix[k][i] *= Weights[k]
        k+=1
                
    IdealBest = []
    IdealWorst = []
    for col in range(0,len(matrix.columns)):
        y = matrix.iloc[0:,[col]].values
        
        if effect[col] == "+" :
            MaxV = max(y)
            MinV = min(y)
            IdealBest.append(MaxV[0])
            IdealWorst.append(MinV[0])
        
        if effect[col] == "-":
            MaxV = max(y)
            MinV = min(y)
            IdealBest.append(MinV[0])
            IdealWorst.append(MaxV[0])
        
    siplus = []
    siminus =[]
        
    for row in range(0,len(matrix)):
        d = 0
        d1 = 0
        r = matrix.iloc[row,0:].values
        for t in range(0,len(r)):
            d += math.pow(r[t]- IdealBest[t],2)
            d1 += math.pow(r[t]- IdealWorst[t],2)
        siplus.append(math.sqrt(d))
        siminus.append(math.sqrt(d1))
            
    PerformanceScore=[]
    for row in range(0,len(matrix)):
        PerformanceScore.append(siminus[row]/siminus[row + siplus[row]])
            
    Toprank = []
    sortedPerformanceScore = sorted(PerformanceScore, reverse = True)
    for row in range(0,len(matrix)):
        for i in range(0,len(matrix)):
            if PerformanceScore[row] == sortedPerformanceScore[i]:
                Toprank.append(i+1)
            
    column1 = df.iloc[:,[0]].values
    matrix.insert(0,df.columns[0],column1)
    matrix['Topsis Score ']= PerformanceScore
    matrix['Rank']= Toprank
            
    Colnewnames = []
    for name in df.columns:
        Colnewnames.append(name)
    Colnewnames.append('Topsis Score')
    Colnewnames.append('Rank')
    matrix.columns=Colnewnames
            
    matrix.to_csv(resultName)
    print(tabulate(matrix,headers=matrix.columns))
            
def parameters():
    if len(sys.argv)==5:
        filename = sys.argv[1].lower()
        Weights = sys.argv[2].split(",")
        for i in range(0, len(Weights)):
          Weights[i] = int(Weights[i])
          
        
        effect = sys.argv[3].split(",")
        FinalFile = sys.argv[-1].lower()
        if ".csv" not in FinalFile:
            print("Result File name should not contain .csv")
        if path.exists(filename):
           if len(Weights)== len(effect):
               topsis(filename,Weights,effect,FinalFile)
           else :
               print("INPUT ERROR!! Number of weights and effects should be same.")
               return
        else :
            print("Check Input, INPUT FILE DOESNOT EXIST")
            return
    else :
      print("Required Number of arguments are not provided")
      print("Input Format : python <script_name> <data> <Weights> <effect> <result>")
      return