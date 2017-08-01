def OctalToDecimal(number):
    i = 1
    decimal = 0
    while (number != 0):
        remainder = number % 10
        number /= 10
        decimal += remainder * i
        i *= 8
    return decimal
    
octalnumber = 957420
print(OctalToDecimal(octalnumber))
