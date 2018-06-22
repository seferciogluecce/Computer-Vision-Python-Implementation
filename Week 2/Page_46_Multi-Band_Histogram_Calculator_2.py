import numpy as np

def histogram(I): #multiband histogram calculation
    
    h,w,d=I.shape
    
    hist=np.zeros([256,d],dtype=np.uint8) #allocate the histogram
    
    for g in range(256):
        hist[g][0] = sum([i.tolist().count(g) for i in I[:,:,0]])
        hist[g][1] = sum([i.tolist().count(g) for i in I[:,:,1]])
        hist[g][2] = sum([i.tolist().count(g) for i in I[:,:,2]])
        
    return hist

#same as page 45 no change