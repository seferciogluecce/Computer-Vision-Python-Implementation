N=[]
# Recursively give label to this pixel 
# and all it foreground neighbours.
def label(x_start,y_start,n,B,L):
    L[y_start][x_start]= n
    for (y,x) in N[y_start][x_start]:
        if L[y][x]==0 and B[y][x]:
            label(x,y,n,B,L)