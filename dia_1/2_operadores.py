numero1= 20
numero2= 40

#aritmeticos
suma = numero1 + numero2 #suma
#resta
resta = numero1 - numero2
#multiplicacion
multiplicacion = numero1 * numero2
#division
division = numero1 / numero2
#division parte entera 
division_entera = numero1 // numero2
#modulo
modulo = numero1 % numero2
#potencia
potencia = numero1 ** numero2

print(division)
print(division_entera)
print(potencia)

# Para poder realizar la raiz se puede hacer uso de la potencia
# numero ** (1/2) > raiz cuadrada
# 1/n donde n sea la raiz a la que se desea buscar
# print(10000 ** (1/10))

print((1/3)/(1/2))
resultado = (1/3)/(1/2)
fraccion = Fraction(resultado).limit_denominator()
print(fraccion)
print(0.3333/0.5)
print(division)
print(division_entera)
print(potencia)

# Comparacion
# Boolean > Verdadero o Falso
# =   > Asignacion
# numero = 30
# ==  > Comparacion
# numero == numero2
# Igual que

print(numero1 == numero2)

# Diferente que
print(numero1 != numero2)

# Mayor que
print(numero1 > numero2)

# Menor que
print(numero1 < numero2)

# Mayor o igual que
print(numero1 >= numero2)

# Menor o igual que
print(numero1 <= numero2)

# Logicos
# and > se tiene que cumplir las dos condiciones para que todo sea verdadero
# or > se tiene que cumplir al menos una condificion para que todo sea verdadero
# not > invierte el resultado de la comparacion (si es V > ahora es F)
print(numero1 > numero2 and numero1 != numero2)
print(numero1 > numero2 or numero1 != numero2)
print(not numero1 > numero2)