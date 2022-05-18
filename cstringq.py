def toStr(n,base):
   global count 
   count += 1
   convertString = "01"
   if n < base:
      #print "convertstring returns the value", 
      return convertString[n]
   else:
      #print "mapping",convertString[n%base]
      #print "In count ", count, ":", "the number is", n//base
      return toStr(n//base,base) + convertString[n%base]


#print(toStr(76904566,2))
#print "Number of times the function is called", count

for i in range (1,11):
    count = 0    
    print (toStr(i,2))
    print "number of times the function is called", count
    print "------"