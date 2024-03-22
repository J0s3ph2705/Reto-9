#Reto 6 punto 3:
#Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente
n=int(input("Número de gallinas? "))
m=int(input("Número de gallos? "))
k=int(input("Número de pollitos? "))
funcion=lambda n,m,k:(n*6)+(k*1)+(m*7)
total=funcion(n,m,k)
print("La masa total es "+str(total)+" kilogramos")

#Reto 6 punto 4:
#Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
p=int(input("Número de panes? "))
m=int(input("Número de bolsas de leche? "))
h=int(input("Número de huevos? "))
b=int(input("Valor del/los billetes? "))
funcion=lambda p,m,h:(p*300)+(m*3300)+(h*350)
costo=funcion(p,m,h)
vueltas=b-costo
if vueltas>0:
  print("Te sobran "+str(vueltas))
else:
  print("Te faltan "+str(vueltas))

#Reto 6 punto 6:
#El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
c=int(input("Contagiados? "))
d=int(input("Días? "))
n=1
while n<=d:
  funcion=lambda c:c*2
  contagiados=funcion(c)
  c=c*2
  n+=1
print("El número de contagiados totales es de "+str(c))
