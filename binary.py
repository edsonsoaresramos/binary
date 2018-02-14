import sys

def binarios_error(message):
	print(message)
	sys.exit()

def binarios_version():
	print("Decodificador de Binário\nNome: binarios.py\nVersão: 1.1")
	sys.exit()

def main(argv):
	letras = "A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z".split("-")
	#binarios = "01110000 01111001 01110100 01101000 01101111 01101110"
	#binarios = "011100000111100101110100011010000110111101101110"
	multiplos = [16, 8, 4, 2, 1]

	binarios = argv

	if binarios.count(' ') == 0:
		c = 1
		binn = []
		for b in binarios:
			if c == 8:
				binn.append(binarios[:8])
				binarios = binarios.replace(binarios[:8], '')
				c = 1
			c += 1
		binarios = binn
	else:
		binarios = binarios.split(" ")

	indice = 0
	for binario in binarios:
	    binarios[indice] = binario[3:]
	    indice += 1

	asciiTmp = 0
	palavra = ""
	for binario in binarios:
		if binario == "00000":
			if palavra != "":
				palavra = str(palavra) + " "
		indiceMultiplo = 0
		for bin in binario:
			if bin == "1":
				asciiTmp = asciiTmp + multiplos[indiceMultiplo]
			indiceMultiplo += 1
		if asciiTmp != 0:
			palavra = palavra + str(letras[asciiTmp-1])
			asciiTmp = 0
	print ('O ASCII para o binario: ' + str(binarios) + ' : \n' + palavra)

if __name__ == "__main__":
	if len(sys.argv) <= 1:
		binarios_error('SyntaxError: argumento esperado.\nUse binarios.py -h para ajuda')
	elif len(sys.argv) > 2:
		binarios_error('SyntaxError: numeros de argumentos passados invalidos.\nUse binarios.py -h para ajuda')
	elif sys.argv[1] == "-h" or sys.argv[1] == "-H":
		print("usage binarios.py <\"<numero binario>\">")
		sys.exit(1)
	elif sys.argv[1] == "-v" or sys.argv[1] == "-V":
		binarios_version()	
	else:
		main(sys.argv[1])