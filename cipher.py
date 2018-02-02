def main():
	alphabet = ['.', ',', '!', '?', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	encoded = input('Enter data here: ')
	encoded = encoded.upper()
	shift = 0
	print(encoded.upper())
	for x in range(0, len(alphabet)):
		shift += 1
		shifted_set = ""
				
		for index in range(shift, len(alphabet)):
			shifted_set += alphabet[index]
			
		for index in range(0, shift-1):
			shifted_set += alphabet[index]
	
		decoded = ""
		
		for letter in encoded:
			index = shifted_set.find(letter)
			decoded += alphabet[index]	
				
		print(decoded)

main()