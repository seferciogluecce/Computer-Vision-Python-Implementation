
N=[]

def label(x_start,y_start,n,B,L):
    L[y_start][x_start]= n
    for (x,y) in N[y_start][x_start]:
        if L[y][x]==0 and B[y][x]:
            label(x,y,n,B,L)
            