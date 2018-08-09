##
import sys
import os
import math
def ex_en():
    f=open("slurm-1881708.out","r")
    A=f.readlines()
    f.close()
    N=len(A)
    count,iList,EN_MAT = 0,[],[]
    for i in xrange(N):
        L=A[i].split()
        if len(L)>0 and L[0]=="ham_el" and L[1]=="=":
            iList.append(i)
            EN_MAT.append([])
            count = count+1
    for i in xrange(count):
        ij=iList[i]
        for j in xrange(3):
            EN_MAT[i].append(float(A[ij+2+j].split()[j])) 
    
    fout = open("Adiabatic_en","w")
    for i in xrange(len(EN_MAT)):
        fout.write(" %i %10.5f %10.5f %10.5f \n"%(i,EN_MAT[i][0],EN_MAT[i][1],EN_MAT[i][2])) #print EN_MAT[i][j]
    fout.close()
##
# Main function calling
ex_en()

