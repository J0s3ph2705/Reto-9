# Reto-9
1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
```python
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
```
2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
```python
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
    

``` 
3. Escriba una función recursiva para calcular la operación de la potencia.
```python
#Se hace la función recursiva
def potencia_recursivo(b:int,p:int)->int:
  return b*(b**(p-1))
#Se toman los datos y se ejecutan en la función, luego se devuelve el resultado
if __name__ == "__main__":
  b=int(input("Base? "))
  p=int(input("Potencia? "))
  potencia=potencia_recursivo(b,p)
  print(str(b)+" elevado a "+str(p)+" es "+str(potencia))
```  
4. Utilice la siguiente plantilla de code para contar el tiempo:
```python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```

Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.
**Importante:** Revisar este [hilo](https://stackoverflow.com/questions/8220801/how-to-use-timeit-module).

5. Crear cuenta en [stackoverflow](https://stackoverflow.com/) y adjuntar imagen en el repo

   Aquí está el link:https://stackoverflow.com/users/23719532/joseph
<div align='center'>
<figure> <img src="https://github.com/J0s3ph2705/Reto-9/assets/159032718/c5f0283a-7620-45ff-8705-05f469af445b" alt="" width="600" height="auto"/></br>
<figcaption><b>Modelo matemático de la comunicación</b></figcaption></figure>
</div>
6. Cosas de adultos....ir a [linkedin](https://www.linkedin.com/) y crear perfil
   
   Aquí está el link: https://www.linkedin.com/in/joseph-lievano-rodriguez-a18238300/
