
def romanToInt(s : str):

	roman = {
		"I" : 1,
		"V" : 5,
		"X" : 10,
		"L" : 50,
		"C" : 100,
		"D" : 500,
		"M" : 1000
	}
	result = 0

	for i in range(len(s)):

		if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]: # i + 1 < len(s) makes sure the last pair are checked without going out of bounds
			result -= roman[s[i]]
		else:
			result += roman[s[i]]

	return result

x = 'CM'

print(romanToInt(x))

