digit    = "0123456789"
array_keywords = []
palabra_actual = ""
array_elementos = []
archivo_recibido = input('Escribe el nombre del archivo a leer (con su extension): ')
file = open(archivo_recibido, 'r')
for line in file:
	for e in line:
		if e == '\n':
			e = ' '
		if e == ' ':
			array_elementos.append(palabra_actual)
			palabra_actual = ''
			e = ''
		palabra_actual += e
array_elementos.append(palabra_actual)
print('Mensaje encontrrado en el documento:'+str(array_elementos))
u = 0
new_array_keywords = []
for line in array_elementos:
	if line in array_keywords:
		print('Se encontro keyword: %s' % line)
		new_array_keywords.append(line)
		array_elementos.pop(u)
	u += 1
key = False
isToken = False
number_of_errors = 0
for line in array_elementos:
	for i in line:
		if key == False:
			if i in digit:
				isToken = True
				key = True
			else:
				isToken = False
				number_of_errors +=1
		if key == True:
			if i in digit:
				isToken = True
			else:
				if isToken == True:
					number_of_errors += 1
	key = False
	if isToken == True and number_of_errors <= 0:
		print('SE ENCONTRO UN TOKEN TIPO: number ')
	number_of_errors = 0
key = False
isToken = False
number_of_errors = 0
for line in array_elementos:
	for i in line:
		if key == False:
			if i in digit:
				isToken = True
				key = True
			else:
				isToken = False
				number_of_errors +=1
		if key == True:
			if i in digit:
				isToken = True
			else:
				if isToken == True:
					number_of_errors += 1
	key = False
	if ',' in line:
		isToken = True
		number_of_errors -= len(',')
	else:
		isToken = False
	if isToken == True and number_of_errors <= 0:
		print('SE ENCONTRO UN TOKEN TIPO: decnumber ')
	number_of_errors = 0


import sys

left_right = []
word = ''
position = 0
array_of_symbols = []
array_of_symbols.append(',')
for line in array_elementos:
	for i in line:
		if i in array_of_symbols:
			word = word.replace(i, '')
			i = i.replace(i, '')
			left_right.append(word)
			word = ''
		word += i

left_right.append(word)
actual=0
for e in array_elementos:
	before = actual
	actual = e
	if actual == before and (actual in array_of_symbols or before in array_of_symbols):
		print('Dos simbolos repetidos')

try:
	def PrintSum ():
		pass
		n = float(left_right[0])
		while len(left_right) > 0:
			n =     Sumatoria(n)
			left_right.pop(0)
		print("La sumatoria de valores en la lista es: %s" %n) 
	def Sumatoria(acumulado) :
		pass
		lista = [acumulado, float(left_right[0])]
		suma = sum(lista)
		return suma 
	PrintSum()
except:
	print('Ocurrio un error.') 
	print('Debe revisar los elementos ingresados')