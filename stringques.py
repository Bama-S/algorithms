def cString(number,b):
   values = "0123456789"
   if number < b:
      return values[number]
   else:
      print "mapping",values[number%b]
      #print "In count ", count, ":", "the number is", n//base
      return cString(number//b,b) + values[number%b]

print (cString(958,10))
