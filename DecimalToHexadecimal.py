def DecimalToHexadecimal(n):
    if n < 16:
        return ToHexadecimal(n)
    temp = n % 16
    n /= 16
    return DecimalToHexadecimal(n) + str(ToHexadecimmal(temp))
    
DECIMALTOHEXADECIMALSINGLEDIGIT = "0123456789ABCDEF"
def ToHexadecimal(n):
    return DECIMALTOHEXADECIMALSINGLEDIGIT[n]
    
decimalnumber = 49175
print(DecimalToHexadecimal(decimalnumber))
