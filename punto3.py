#Se hace la función recursiva
def potencia_recursivo(b:int,p:int)->int:
  return b*(b**(p-1))
#Se toman los datos y se ejecutan en la función, luego se devuelve el resultado
if __name__ == "__main__":
  b=int(input("Base? "))
  p=int(input("Potencia? "))
  potencia=potencia_recursivo(b,p)
  print(str(b)+" elevado a "+str(p)+" es "+str(potencia))
