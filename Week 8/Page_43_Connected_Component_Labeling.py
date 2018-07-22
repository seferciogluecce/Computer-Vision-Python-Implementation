import numpy as np

N=[]

def label(x_start,y_start,n,B,L):
    L[y_start][x_start]= n
    for (x,y) in N[y_start][x_start]:
        if L[y][x]==0 and B[y][x]:
            label(x,y,n,B,L)
           
            
def ConnectedComponents(B):
    X,Y = B.shape
    L = np.zeros([X,Y])
    n=1
    for (x,y) in B:
        if B[y][x] and L[y][x]==0:
            label(x,y,n,B,L)
            n = n + 1