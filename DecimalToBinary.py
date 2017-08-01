def DecimalToBinary(n):
   if n > 1:
       DecimalToBinary(n//2)
   print(n % 2,end = '')

decimalnumber = 109069
DecimalToBinary(decimalnumber)
