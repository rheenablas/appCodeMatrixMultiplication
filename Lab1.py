#matrix multiplication
#derived by https://www.programiz.com/python-programming/examples/multiply-matrix


import time
import random as r

def generateMatrix(number):
    matrix = []

    for i in range(number):
        innerList = []
        for y in range(number):
            innerList.append(r.randint(0, 100))
        matrix.append(innerList)
        
        
    return matrix

def generateEmptyMatrix(number):
    matrix = []

    for i in range(number):
        innerList = []
        for y in range(number):
            innerList.append(0)
        matrix.append(innerList)
        
        
    return matrix
        

numberList = [30, 50, 80, 100, 150]

executionTimeList = []

#make matrix
for index in numberList:
    startTime = time.time()
    for i in range(2, index+1):
    #a timer
        
        firstMatrix = generateMatrix(i)
        secondMatrix = generateMatrix(i)
        resultMatrix = generateEmptyMatrix(i)
        #calculate matrix
        for k in range(i):
            for l in range(i):
                for m in range(i):
                    resultMatrix[k][l] += firstMatrix[k][m]* secondMatrix[k][l]
        

    #timer end time
    endTime = time.time() - startTime
    executionTimeList.append(endTime)
    print(f'Value size: {index} - execution time: {endTime}')









