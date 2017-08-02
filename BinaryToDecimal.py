def BinaryToDecimal(number):
	b = list(number)
	n = len(list(number))
	decimal = 0
	temp = 0
	i = 0
	exp = n-1
	while (i < n):
		x = int(b[i])
		quot= 2**exp
		temp = x*quot
		i += 1
		exp -= 1
		decimal = decimal + temp
	return(decimal)
