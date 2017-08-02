def HexadecimalToDecimal(n):
    DECIMALTOHEXADECIMALSINGLEDIGIT = "0123456789ABCDEF"

    if not all([var in DECIMALTOHEXADECIMALSINGLEDIGIT for var in n.upper()]):
        print "Invalid string"
        return None

    return sum([DECIMALTOHEXADECIMALSINGLEDIGIT.find(var) * 16 ** i for i, var in enumerate(reversed(n.upper()))])
