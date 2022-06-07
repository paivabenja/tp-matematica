# Lo primero que haremos sera seccionar el string donde se aloja la funcion ingresada por el usuario para trabajar cada una de las secciones.

# Supongamos que el usuario ingresó: F(x)=x**2/x+3 como string y = como carácter,
# La función "section" la dividira en dos strings: "F(x)" y "x**2/x+3"

dsadsa = 3

mod = [
  'x' ,  #0
  'y' ,  #1
  '+' ,  #2
  '-' ,  #3
  '(' ,  #4
  ')' ,  #5
  '=' ,  #6
  '**',  #7
  '/' ,  #8
]

def section (string, char, intr=-1):
  section = string.split(char)
  if intr!=-1 :
    return (section[intr])
  else:
    return (section)

equivalencias = section('F(x)=x**2/x+3', mod[6])
print ('equivalencia 1: ', equivalencias[0])
print ('equivalencia 2: ', equivalencias[1])

# Aplicando la funcion section repetidas veces variando los valores del caracter podemos dividir cada funcion hasta obtener cada valor individualmente
dividendo= section(equivalencias[1], mod[8],0)
print ('dividendo: ', dividendo)

divisor= section(equivalencias[1], mod[8],1)
print ('divisor: ', divisor)