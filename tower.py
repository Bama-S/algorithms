def moveTower(height,A1, A3, A2):
    if height >= 1:
        print A1,A2,A3
        moveTower(height-1,A1,A2,A3)
        print "ttt", A1,A2,A3
        moveDisk(A1,A3)
        moveTower(height-1,A2,A3,A1)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"1","3","2")