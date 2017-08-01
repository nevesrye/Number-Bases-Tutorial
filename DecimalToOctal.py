def DecimalToOctal(number):
    i = 1
    octal = 0
    while (number != 0):
        reminder = number % 8
        number /= 8
        octal += reminder * i
        i *= 10
    return octal

decimalnumber = 49175
print(DecimalToOctal(decimalnumber))
