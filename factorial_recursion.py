def recursive (n):
    global t
    print "factorial has been called with n =", str(n)
    if n ==1:
        return 1
    else:
        res = n*recursive(n-1)
        print "Intermediate result of factorial", res
        return res

t = 1
recursive(3)
