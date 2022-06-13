# Lo primero que haremos sera seccionar el string donde se aloja la funcion ingresada por el usuario para trabajar cada una de las secciones.

# Supongamos que el usuario ingresó: F(x)=x**2/x+3 como string y = como carácter,
# La función "section" la dividira en dos strings: "F(x)" y "x**2/x+3"

class Function ():
	def option(selection=int(input('''Ingrese el número correspondiente a la función:
	1- función racional
	2- función racional
	3- función racional
	4- función racional
	'''))):

		if (selection == 1):
			return 'racional'

	def __init__ (self, type = option() , value):
		self.type = type
		self.value = value

	def section(string, char, intr=-1):
	    section = string.split(char)
	    if intr != -1:
	        return (section[intr])
	    else:
	        return (section)

if __name__ == '__main__':
	func = Function('F(x) = x**2')
	print func.type