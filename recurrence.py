def recur(a):
    if len(a)>1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        print "left: ", left
        print "right: ", right       
        recur(left)
        recur(right)
a = [5,3,4,2,1,0,4,5,7,89,53]
recur(a)