import sys

def binary_error(message):
	print(message)
	sys.exit()

def binary_version():
	print('** Binary Decode **\nName: binary.py\nVersion: 1.0.1')
	sys.exit()

def binary_help():
	print('*** Binary Decode Help ***')
	print("usage binary.py <\"<Binary Number>\">")
	sys.exit(1)		

def main(argv):
	letters = "A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z".split("-")
	#binaryExample = "01110000 01111001 01110100 01101000 01101111 01101110"
	#binaryExample = "011100000111100101110100011010000110111101101110"
	multiples = [16, 8, 4, 2, 1]

	binary = argv

	if binary.count(' ') == 0:
		c = 1
		binn = []
		for b in binary:
			if c == 8:
				binn.append(binary[:8])
				binary = binary.replace(binary[:8], '')
				c = 1
			c += 1
		binary = binn
	else:
		binary = binary.split(" ")

	indexx = 0
	for bina in binary:
	    binary[indexx] = bina[3:]
	    indexx += 1

	asciiTmp = 0
	word = ""
	for bina in binary:
		indexMultiple = 0
		for bin in bina:
			if bin == "1":
				asciiTmp = asciiTmp + multiples[indexMultiple]
			indexMultiple += 1
		if asciiTmp != 0:
			word = word + str(letters[asciiTmp-1])
			asciiTmp = 0
	print ('The ASCII result to binary is: ' + str(binary) + ' : \n' + word)

if __name__ == "__main__":
	if len(sys.argv) <= 1:
		binary_error('SyntaxError: Expected Argument.\nUse binary.py -h for help')
		sys.exit()
	elif len(sys.argv) > 2:
		binary_error('SyntaxError: Invalid Number of Arguments.\nUse binary.py -h for help')
		sys.exit()
	elif sys.argv[1] == "-h" or sys.argv[1] == "-H":
		binary_help()
	elif sys.argv[1] == "-v" or sys.argv[1] == "-V":
		binary_version()
	else:
		main(sys.argv[1])