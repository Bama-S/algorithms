#log n base 2
import matplotlib.pyplot as plt



def findlog(n):
    i = n
    loop = 0
    while i > 0:
        loop += 1       
        #print i
        i = i //2
    return loop
    
a1 = findlog(8)
a2 = findlog(16)
a3 =  findlog(32)
a4 = findlog(64)
a5 = findlog(128)
a6 = findlog(256)
a7 = findlog(512)
a8 = findlog(1024)
a9 = findlog(2048)

x = [8,16,32,64,128,256,512,1024,2048]
x1 = [8/2,16/2,32/2,64/2,128/2,256/2,512/2,1024/2,2048/2]
y = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
plt.plot(x,y,color = "blue", linewidth = 1.0, linestyle = "-")
plt.plot(x1,y,color = "green", linewidth = 1.0, linestyle = "-")
plt.show()