#Guassian elimination
import numpy as np
import sys
n = 3
#a_dash = np.zeros((n,n+1))
#print(a_dash)
x=np.zeros(n)
print (x)
# Reading augmented matrix coefficients
print('Enter Augmented Matrix Coefficients:')
a_dash = np.array([[3,1,1,11],[6,4,1,29],[1,1,1,7]])
print(a_dash)
a = a_dash.astype(np.float)
x = x.astype(np.float)
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]

        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]
print(a)
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]

    x[i] = x[i]/a[i][i]
print(x)
