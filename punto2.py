#Reto 6 punto 3:
#Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente
def sumar_masa(*args)->int:
  suma:int=0
  for num in args:
    suma+=num
  return suma
if __name__ == "__main__":
  n=int(input("Número de gallinas? "))
  m=int(input("Número de gallos? "))
  k=int(input("Número de pollitos? "))
  g=n*6
  l=m*7
  print("La masa total es "+str(sumar_masa(l,g,k))+" kilogramos")

#Reto 6 punto 4:
#Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
def sumar_costo(*args)-> int:
  suma : int = 0
  for num in args:
    suma +=  num
  return suma
if __name__ == "__main__":
  p=int(input("Número de panes? "))
  m=int(input("Número de bolsas de leche? "))
  h=int(input("Número de huevos? "))
  b=int(input("Valor del/los billetes? "))
  p=p*300
  m=m*3300
  h=h*350
  costo=sumar_costo(p,m,h)
  vueltas=b-costo
  if vueltas>0:
    print("Te sobran "+str(vueltas))
  else:
    print("Te faltan "+str(vueltas))

#Reto 6 punto 6:
#El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
def duplicacion(*args)-> int:
  doble : int = 0
  for num in args:
    doble=num*2
  return doble
n=1
if __name__ == "__main__":
  c=int(input("Contagiados? "))
  d=int(input("Días? "))
  while n<=d:
    c=duplicacion(c)
    n+=1
print("El número de contagiados totales es de "+str(c))
    
