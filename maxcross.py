def maxcross(a):
    leftsum = -99999
    sum = 0
    mid = len(a)//2
    for i in range(mid,0,-1):
        sum = sum +a[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i
    rightsum = -99999
    sum = 0
    for j in range(mid+1,len(a)):
        sum = sum +a[j]
        if sum >rightsum:
            rightsum = sum
            maxright = j
    print maxleft, maxright, leftsum+rightsum




a = [-10,5,3,-4,2,-3,7,1,2,-5]
maxcross(a)