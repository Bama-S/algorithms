def maxcross(a,low,high):
    if len(a) > 1:
        mid = len(a) //2
        leftsum = -99999
        sum = 0
        for i in range(mid,low,-1):
            sum = sum +a[i]
            print sum
            if sum > leftsum:
                leftsum = sum
                maxleft = i
        rightsum = -99999
        sum = 0
        if mid+1 < high:
            for j in range(mid,len(a)):
                sum = sum +a[j]
                if sum >rightsum:
                    rightsum = sum
                    maxright = j
        print maxleft, maxright, leftsum+rightsum


def maxsubarray(a,low,high):
    if len(a) >1:
        mid = len(a)//2        
        leftlow,lefthigh = low,mid
        print "leftlow", leftlow
        print "lefthigh", lefthigh
        leftarray = a[leftlow:lefthigh]
        print "leftarray", leftarray
        maxsubarray(leftarray,leftlow,lefthigh)
        rightlow,righthigh = mid,high
        print "rightlow", rightlow
        print "righthigh", righthigh
        rightarray = a[rightlow:righthigh]
        print "rightarray", rightarray
        maxsubarray(rightarray,rightlow,righthigh)
        print a, low, mid, high
        #maxcross(a,low,high)


a = [-10,5,3,-4,2,-3,7,1,2,-5]
maxsubarray(a,0,len(a))
#maxcross(a,0,5,10)
