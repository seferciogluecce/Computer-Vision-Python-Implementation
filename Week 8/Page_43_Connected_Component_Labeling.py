import numpy as np

N=[]

# Recursively give label to this pixel 
# and all it foreground neighbours.
def label(x_start,y_start,n,B,L):
    L[y_start][x_start]= n
    for (y,x) in N[y_start][x_start]:
        if L[y][x]==0 and B[y][x]:
            label(x,y,n,B,L)      
           
#B is the binary image input.
#L is the labeled image output         
def ConnectedComponents(B):
    X,Y = B.shape
    L = np.zeros([X,Y])
    n=0
    for (y,x) in B:
        if B[y][x] and L[y][x]==0:
            label(x,y,n,B,L)
            n = n + 1
    return L 