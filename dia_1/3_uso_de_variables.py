# snake_case 
nombre_completo = 'wilder larry'

# camelcase 
nombrecompleto = 'wilder larry'

#pascalcase
nombrecompleto = 'wilder larry'

#los nombres de las variables no pueden conter caracterss especailes '-' '@' '/' y simbolos
# sombre@completo = 'eduardo de rivero'

# tampoco puede empezar con numeros
nombre1 = 'wilder'
nombre2 = 'larry'

# al hacer sumas de strings esto se hace una concatenacion
# solamente la suma puede ser entre strings o int o float mas no combinarlos
resultado = 'fabiola' + 'roberta'

print (resultado)

#nombre podemos acceder a los strings en base a sus posiciones 
nombre = 'pedrito'
print(nombre[3])

#solamente se puede vosualizar el texto en sus posiciones mas no modificarlos 
# inmutables (no se puede mutar o modificar)
# nombre [6] = 'a'

#para saber la longitud del texto 
longitud = len(nombre)
print(longitud)

#se puede sacar aun sub string o una sub-cadena
texto = 'el dia de hoy me levante y fui a marchar por mi pais y de ahi me comi un pan con tiburon'

sub_texto = texto[3:17]

print (sub_texto)
# empieza desde el inicio hasta la posicion <17
sub_texto = texto[:17]
print (sub_texto)

sub_texto = texto[23:]
print(sub_texto)

# si colocamos [:] haremoa una copia del contenido de la variable texto
sub_texto = texto [:]
sub_texto = texto
print(sub_texto)

#numerico
resultado = 10+3.75
#forma para poder hacer mas aleible un numero grande con las adherencias de '_', esto sirve solamente para lectura 
# esta ayuda esta disponible desde la version 3.6 de python en adelante
numerazo = 1_010_101_010
print (resultado)

print (resultado)

numero1, numero2, numero3 =3, 'juliaca', true, 4.5
print(numero1)
print(numero2)

#boolean 
libre = true 
#en python para utilizar el operador '!' se tiene que utilizar el operador 'not'
print (not libre)
