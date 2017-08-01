def OctalToDecimal(number):
    i = 1
    decimal = 0
    while (number != 0):
        reminder = number % 10
        number /= 10
        decimal += reminder * i
        i *= 8
    return decimal
    
octalnumber = 957420
print(OctalToDecimal(octalnumber))
