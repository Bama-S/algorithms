#-*- coding: utf-8 -*-
import sys, time

def gk(i,j):
    return str(i)+','+str(j)

def matrix_chain_order(p):
    n = len(p)-1
    m, s = {}, {}
    for i in xrange(1, n+1):
        m[gk(i, i)] = 0
    for l in xrange(2, n+1):
        for i in xrange(1, n-l+2):
            j = i+l-1
            m[gk(i, j)] = sys.maxint
            for k in xrange(i, j):
                q = m[gk(i, k)]+m[gk(k+1, j)]+p[i-1]*p[k]*p[j]
                if q<m[gk(i, j)]:
                    m[gk(i, j)] = q
                    s[gk(i, j)] = k
    return m, s

def get_optimal_parens(s, i, j):
    res = ''
    if i == j:
        return "A"+str(j)
    else:
        res += "("
        res += get_optimal_parens(s, i, s[gk(i, j)])
        res += get_optimal_parens(s, s[gk(i, j)]+1, j)
        res +=  ")"
        return res

def main():
    p = [5,4,6,2,7]
    m, s = matrix_chain_order(p)
    print 'minmatrix', m
    print 'smatrix',s
    print 'Optimal multiplication：', m[gk(1, len(p)-1)]
    print 'Order of multiplication', get_optimal_parens(s, 1, len(p)-1)

if __name__ == '__main__':
    b = time.time()
    main()
    print 'total run time is:', time.time()-b