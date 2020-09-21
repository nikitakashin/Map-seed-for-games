
seed_length = 24
chars_array = []



def get_seed(a):
	char = 0
	for i in a:
		b = standart_chars.get('str(a[i])', 69)
		chars_array.append(b)
	if len(chars_array) > 4:
		c = (chars_array[0] + 2 * chars_array[1]) / (11 * (chars_array[2] + chars_array[3]))
		k = 0
		for i in chars_array:
			c = c * 1.42069143 * chars_array[k]
			k += 1
	else:
		c = (228 * chars_array[0] - 420) * 0.142
		k = 0
		for i in chars_array:
			c = c * 1.42069143 * chars_array[k]
			k += 1
	c = round(c)
	while(len(str(c)) != seed_length):
		if len(str(c)) > seed_length:
			c = c / 11.352
			c = round(c)
		elif len(str(c)) < seed_length:
			c = c * 11.352
			c = round(c)
		elif len(str(c)) == seed_length:
			c = round(c)
	return c
	






standart_chars = {
	'a': 10,
	'b': 10,
	'c': 10,
	'd': 10,
	'e': 10,
	'f': 10,
	'g': 10,
	'h': 10,
	'i': 10,
	'j': 10,
	'k': 10,
	'l': 10,
	'm': 10,
	'n': 10,
	'o': 10,
	'p': 10,
	'q': 10,
	'r': 10,
	's': 10,
	't': 10,
	'u': 10,
	'v': 10,
	'w': 10,
	'x': 10,
	'y': 10,
	'z': 10,
	'а': 10,
	'б': 10,
	'в': 10,
	'г': 10,
	'д': 10,
	'е': 10,
	'ё': 10,
	'ж': 10,
	'з': 10,
	'и': 10,
	'й': 10,
	'к': 10,
	'л': 10,
	'м': 10,
	'н': 10,
	'о': 10,
	'п': 10,
	'р': 10,
	'с': 10,
	'т': 10,
	'у': 10,
	'ф': 10,
	'х': 10,
	'с': 10,
	'ч': 10,
	'ш': 10,
	'щ': 10,
	'ъ': 10,
	'ы': 10,
	'ь': 10,
	'э': 10,
	'ю': 10,
	'я': 10,
	'0': 10,
	'1': 10,
	'2': 10,
	'3': 10,
	'4': 10,
	'5': 10,
	'6': 10,
	'7': 10,
	'8': 10,
	'9': 10,
	'"': 10,
	'№': 10,
	';': 10,
	'%': 10,
	':': 10,
	'?': 10,
	'*': 10,
	'(': 10,
	')': 10,
	'_': 10,
	'+': 10,
	'=': 10,
	'-': 10,
	'&': 10,
	'^': 10,
	'$': 10,
	'#': 10,
	'@': 10,
	']': 10,
	'[': 10,
	'}': 10,
	'{': 10,
	'|': 10,
	'/': 10,
	'\\': 10,
	'\'': 10,
	'.': 10,
	',': 10,
	'>': 10,
	'<': 10,
	'`': 10,
	'~': 10,

}


e = get_seed('1')
print(e)