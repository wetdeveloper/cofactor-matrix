import numpy as np
import math
C=[
    [1,-1,0,0],
    [-1,3,-1,-1],
    [0,-1,2,-1],
    [0,-1,-1,2]
]

C1=[
    [1,2,3],[4,5,6],[7,8,9]
]

C2=[[1,2],[3,4]]

C3=[
    [1,2,3,4,5],
    [5,6,7,8,9],
    [10,11,12,13,14]
]

C4=[
    [1,-1,0,0],
    [-1,3,-1,-1],
    [0,-1,2,-1],
    [0,-1,-1,2]
]

C5=[
    [0,0,0,0],
    [0,6,1,1],
    [0,4,-2,5],
    [0,2,8,7]
]

C6=[
    [5]
]

c7=[
    [2,3]
]


def determinant(matrix,i,j):
    #matrix n*m  row=i col=j   1<=i<=m   1<=j<=m 
    #i=0,j=0-->returns full matrix determinant
    if i>=0 and j>=0 and len(matrix)>1:
        M=[]
        for I in range(len(matrix)):
            if I!=i-1:
                temp=[]
                for J in range(len(matrix[I])):
                    if J!=(j-1):
                        temp.append(matrix[I][J])
                M.append(temp)
        try:
            det = np.linalg.det(M)
        except np.linalg.LinAlgError as e:#rows!=columns
            colsnum=len(M[0])
            while len(M)!=colsnum:
                M.append([0 for i in range(len(M[0]))])
            det = np.linalg.det(M)
        return det
    else:
        return AssertionError("correct your matrix and try again")
    

def cofactor(matrix):
    matrix_cofac={}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix_cofac[f'm{i+1}{j+1}']=math.pow(-1,i+j)*determinant(matrix, i+1, j+1)
    return matrix_cofac


# print(determinant(C5, 1, 1))
# print(determinant(C2, 0, 0))
# print(cofactor(C4))
# print(cofactor(C5))
# print(cofactor(C2))
#print(determinant(C6, 0, 0))
# print(determinant(c7, 1, 1))
# print(determinant(c7, 0, 0))



            
