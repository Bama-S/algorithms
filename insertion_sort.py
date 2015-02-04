a = [5,2,4,6,1,3]
num = len(a)
for j in range(1,num):
    key = a[j]
    i = j-1
    while (i>=0) and (a[i]>key):
        print a[i+1]    
        a[i+1]=a[i]
        print "inter", a
        i = i-1
        print "i", i
        print "ttt", a[i],a[i+1]
        print "key", key    
    a[i+1] = key
    print i+1
    print "a[i+1]", a[i+1]
    print a
    

