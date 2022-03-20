import numpy as np

def coefficient(k,t,n):
    # Generate the coefficient matrix for (1+x+x^2+...+x^k)^t
    # Check condition for inputs
    CM = np.full([t+1,n+1],0)
    CM[0,0] = 1
    for i in range(1,t+1):
        for j in range(0,n+1):
            lb = max(0,j-k)
            for l in range (lb,j+1):
                CM[i,j] = CM[i,j] + CM[i-1,l]
    return CM[t,n]
    
