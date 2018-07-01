

I=[]
B=[]
Y=0
X=0
T=0

for y in range(0,Y):
    for x in range(0,X):
        if I[y][x]>=T:
            B[y][x]= 1
        else:
            B[y][x]=0